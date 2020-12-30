import Vue from 'vue'
import Router from 'vue-router'

Vue.use(Router)

/* Layout */
import Layout from '@/layout'

/**
 * Note: sub-menu only appear when route children.length >= 1
 * Detail see: https://panjiachen.github.io/vue-element-admin-site/guide/essentials/router-and-nav.html
 *
 * hidden: true                   if set true, item will not show in the sidebar(default is false)
 * alwaysShow: true               if set true, will always show the root menu
 *                                if not set alwaysShow, when item has more than one children route,
 *                                it will becomes nested mode, otherwise not show the root menu
 * redirect: noRedirect           if set noRedirect will no redirect in the breadcrumb
 * name:'router-name'             the name is used by <keep-alive> (must set!!!)
 * meta : {
    roles: ['admin','editor']    control the page roles (you can set multiple roles)
    title: 'title'               the name show in sidebar and breadcrumb (recommend set)
    icon: 'svg-name'/'el-icon-x' the icon show in the sidebar
    breadcrumb: false            if set false, the item will hidden in breadcrumb(default is true)
    activeMenu: '/example/list'  if set path, the sidebar will highlight the path you set
  }
 */

/**
 * constantRoutes
 * a base page that does not have permission requirements
 * all roles can be accessed
 */
export const constantRoutes = [
  {
    path: '/login',
    component: () => import('@/views/login/index'),
    hidden: true
  },

  {
    path: '/404',
    component: () => import('@/views/404'),
    hidden: true
  },

  {
    path: '/',
    component: Layout,
    redirect: '/dashboard',
    children: [{
      path: 'dashboard',
      name: 'Dashboard',
      component: () => import('@/views/dashboard/index'),
      meta: { title: '图书管理系统', icon: 'el-icon-s-help' }
    }]
  },

  {
    path: '/book',
    component: Layout,
    redirect: '/test/book',
    children: [
      {
        path: 'book',
        name: 'book',
        component: () => import('@/views/test/book'),
        meta: { title: '馆藏展示', icon: 'table' }
      }
    ]
  },
  {
    path: '/addBook',
    component: Layout,
    redirect: '/test/addBook',
    children: [
      {
        path: 'addBook',
        name: 'addBook',
        component: () => import('@/views/test/addBook'),
        meta: { title: '新增图书', icon: 'nested' }
      }
    ]
  },
  {
    path: '/deleteBook',
    component: Layout,
    redirect: '/test/deleteBook',
    children: [
      {
        path: 'deleteBook',
        name: 'deleteBook',
        component: () => import('@/views/test/deleteBook'),
        meta: { title: '删除图书', icon: 'nested' }
      }
    ]
  },
  {
    path: '/borrow',
    component: Layout,
    redirect: '/test/borrow',
    children: [
      {
        path: 'borrow',
        name: 'borrow',
        component: () => import('@/views/test/borrow'),
        meta: { title: '借书', icon: 'form' }
      }
    ]
  },
  {
    path: '/breturn',
    component: Layout,
    redirect: '/test/breturn',
    children: [
      {
        path: 'breturn',
        name: 'breturn',
        component: () => import('@/views/test/breturn'),
        meta: { title: '还书', icon: 'link' }
      }
    ]
  },
  {
    path: '/interview',
    component: Layout,
    redirect: '/interview/index',
    children: [
      {
        path: 'interview',
        name: 'interview',
        component: () => import('@/views/interview/index'),
        meta: { title: '采访', icon: 'link' }
      }
    ]
  },
  {
    path: '/catalogue',
    component: Layout,
    redirect: '/catalogue/index',
    children: [
      {
        path: 'catalogue',
        name: 'catalogue',
        component: () => import('@/views/catalogue/index'),
        meta: { title: '编目', icon: 'link' }
      }
    ]
  },
  {
    path: '/up',
    component: Layout,
    redirect: '/excel/up',
    children: [
      {
        path: 'catalogue',
        name: 'catalogue',
        component: () => import('@/views/excel/upload-excel.vue'),
        meta: { title: '编目', icon: 'link' }
      }
    ]
  },
  // {
  //   path: '/example',
  //   component: Layout,
  //   redirect: '/example/table',
  //   name: 'Example',
  //   meta: { title: 'Example', icon: 'el-icon-s-help' },
  //   children: [
  //     {
  //       path: 'table',
  //       name: 'Table',
  //       component: () => import('@/views/table/index'),
  //       meta: { title: 'Table', icon: 'table' }
  //     },
  //     {
  //       path: 'tree',
  //       name: 'Tree',
  //       component: () => import('@/views/tree/index'),
  //       meta: { title: 'Tree', icon: 'tree' }
  //     }
  //   ]
  // },

  // {
  //   path: '/form',
  //   component: Layout,
  //   children: [
  //     {
  //       path: 'index',
  //       name: 'Form',
  //       component: () => import('@/views/form/index'),
  //       meta: { title: 'Form', icon: 'form' }
  //     }
  //   ]
  // },

  // {
  //   path: '/nested',
  //   component: Layout,
  //   redirect: '/nested/menu1',
  //   name: 'Nested',
  //   meta: {
  //     title: 'Nested',
  //     icon: 'nested'
  //   },
  //   children: [
  //     {
  //       path: 'menu1',
  //       component: () => import('@/views/nested/menu1/index'), // Parent router-view
  //       name: 'Menu1',
  //       meta: { title: 'Menu1' },
  //       children: [
  //         {
  //           path: 'menu1-1',
  //           component: () => import('@/views/nested/menu1/menu1-1'),
  //           name: 'Menu1-1',
  //           meta: { title: 'Menu1-1' }
  //         },
  //         {
  //           path: 'menu1-2',
  //           component: () => import('@/views/nested/menu1/menu1-2'),
  //           name: 'Menu1-2',
  //           meta: { title: 'Menu1-2' },
  //           children: [
  //             {
  //               path: 'menu1-2-1',
  //               component: () => import('@/views/nested/menu1/menu1-2/menu1-2-1'),
  //               name: 'Menu1-2-1',
  //               meta: { title: 'Menu1-2-1' }
  //             },
  //             {
  //               path: 'menu1-2-2',
  //               component: () => import('@/views/nested/menu1/menu1-2/menu1-2-2'),
  //               name: 'Menu1-2-2',
  //               meta: { title: 'Menu1-2-2' }
  //             }
  //           ]
  //         },
  //         {
  //           path: 'menu1-3',
  //           component: () => import('@/views/nested/menu1/menu1-3'),
  //           name: 'Menu1-3',
  //           meta: { title: 'Menu1-3' }
  //         }
  //       ]
  //     },
  //     {
  //       path: 'menu2',
  //       component: () => import('@/views/nested/menu2/index'),
  //       name: 'Menu2',
  //       meta: { title: 'menu2' }
  //     }
  //   ]
  // },

  // {
  //   path: 'external-link',
  //   component: Layout,
  //   children: [
  //     {
  //       path: 'https://panjiachen.github.io/vue-element-admin-site/#/',
  //       meta: { title: 'External Link', icon: 'link' }
  //     }
  //   ]
  // },

  // 404 page must be placed at the end !!!
  { path: '*', redirect: '/404', hidden: true }
]

const createRouter = () => new Router({
  // mode: 'history', // require service support
  scrollBehavior: () => ({ y: 0 }),
  routes: constantRoutes
})

const router = createRouter()

// Detail see: https://github.com/vuejs/vue-router/issues/1234#issuecomment-357941465
export function resetRouter() {
  const newRouter = createRouter()
  router.matcher = newRouter.matcher // reset router
}

export default router
