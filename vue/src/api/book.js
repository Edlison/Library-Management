import request from '@/utils/request'

export function getBook() {
  return request({
    url: '/getbook',
    method: 'post'
  })
}