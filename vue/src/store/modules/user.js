import { login, logout, getInfo } from '@/api/user'
import { getToken, setToken, removeToken } from '@/utils/auth'
import { resetRouter } from '@/router'

const getDefaultState = () => {
  return {
    token: getToken(),
    name: '',
    avatar: ''
  }
}

const state = getDefaultState()

const mutations = {
  RESET_STATE: (state) => {
    Object.assign(state, getDefaultState())
  },
  SET_TOKEN: (state, token) => {
    state.token = token
  },
  SET_NAME: (state, name) => {
    state.name = name
  },
  SET_AVATAR: (state, avatar) => {
    state.avatar = avatar
  }
}

const actions = {
  // user login
  login({ commit }, userInfo) {
    console.log("登录测试1")
    console.log(userInfo,"userinfo");
    const { username, password } = userInfo
    return new Promise((resolve, reject) => {
        let formData = new FormData();
        formData.append('user_name',username);
        formData.append('user_password',password);
      // login({ user_name: username.trim(), user_password: password }).then(response => {
        login(formData).then(response => {
        console.log(111);
        console.log(response,"xiangying")
        const { data } = response
        console.log(data,"dataces");
        commit('SET_TOKEN', data.user_role)
        setToken(data.user_role)
        resolve()
      }).catch(error => {
        reject(error)
      })
    })
  },

  // get user info
  getInfo({ commit, state }) {

    return new Promise((resolve, reject) => {
      getInfo(state.token).then(response => {
        const { data } = response
        console.log(response,"res测试11")
        if (!data) {
          // console.log(response,"res测试")
          return reject('Verification failed, please Login again.')
        }

        const { user_name, avatar } = data
        console.log(user_name)
        commit('SET_NAME', user_name)
        commit('SET_AVATAR', avatar)
        resolve(data)
      }).catch(error => {
        reject(error)
      })
    })
  },

  // user logout
  logout({ commit, state }) {
    return new Promise((resolve, reject) => {
      logout(state.token).then(() => {
        removeToken() // must remove  token  first
        resetRouter()
        commit('RESET_STATE')
        resolve()
      }).catch(error => {
        reject(error)
      })
    })
  },

  // remove token
  resetToken({ commit }) {
    return new Promise(resolve => {
      removeToken() // must remove  token  first
      commit('RESET_STATE')
      resolve()
    })
  }
}

export default {
  namespaced: true,
  state,
  mutations,
  actions
}

