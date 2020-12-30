import request from '@/utils/request'

export function addBook(data) {
  return request({
    url: '/addbook',
    method: 'post',
    data,
  })
}