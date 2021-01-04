import request from '@/utils/request'

export function login(data) {
  return request({
    // url: '/vue-admin-template/user/login',
    url: '/api/user/login',
    method: 'post',
    data,
    header:{"Content-Type":"multipart/form-data"}
  })
}

export function getInfo(token) {
  return request({
    // url: '/vue-admin-template/user/info',
    url:'/api/user/get_info',
    method: 'post',
    // params: { token }
  })
}

export function logout() {
  return request({
    url: '/vue-admin-template/user/logout',
    method: 'post'
  })
}
