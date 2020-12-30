import request from '@/utils/request'

export function borrow(data) {
  return request({
    url: '/borrow',
    method: 'post',
    data,
  })
}