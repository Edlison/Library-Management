import request from '@/utils/request'
//还需要改
export function singleCata(data) {
  return request({
    url: '/addbook',
    method: 'post',
    data,
  })
}

export function Cata(data) {
  return request({
    url: '//api/catalog/addcatalog_list/',
    method: 'post',
    data,
  })
}