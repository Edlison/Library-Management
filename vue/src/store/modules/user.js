import { login, logout, getInfo } from '@/api/user'
import { getToken, setToken, removeToken } from '@/utils/auth'
import { resetRouter } from '@/router'

const getDefaultState = () => {
  return {
    token: getToken(),
    name: '',
    avatar: '',
    roles: []//动态路由修改标记
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
  SET_NAME: (state, user_name) => {
    state.name = user_name
  },
  SET_AVATAR: (state, avatar) => {
    state.avatar = avatar
  },
  SET_ROLES: (state, user_role) => {
    state.roles = user_role
  }//动态路由修改标记
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
        console.log(response,"xiangying")
        if(response.status==1){
          reject(response.msg)
        }
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
    console.log("getinfo")
    return new Promise((resolve, reject) => {
      getInfo(state.token).then(response => {
        const { data } = response
        console.log(response,"res测试11")
        if (!data) {
          // console.log(response,"res测试")
          return reject('Verification failed, please Login again.')
        }
        const { user_role,user_name, avatar } = data
        console.log(user_name,"name")
        commit('SET_NAME', user_name)
        commit('SET_ROLES', user_role)
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

