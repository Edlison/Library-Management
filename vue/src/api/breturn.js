import request from '@/utils/request'

export function breturn(data) {
  return request({
    url: '/breturn',
    method: 'post',
    data,
  })
}