import request from '@/utils/request'

export function deleteBook(data) {
  return request({
    url: '/delete',
    method: 'post',
    data,
  })
}