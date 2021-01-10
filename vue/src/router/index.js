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
      meta: { title: '图书管理系统', icon: 'library' }
    }]
  },

  // {
  //   path: '/reader',
  //   component: Layout,
  //   redirect: '/reader',
  //   name: 'reader',
  //   meta: { title: '读者系统', icon: 'reader' },
  //   children: [
  //     {
  //       path: 'book',
  //       name: 'book',
  //       component: () => import('@/views/reader/book'),
  //       meta: { title: '馆藏展示', icon: 'book' }
  //     },
  //     {
  //       path: 'interview',
  //       name: 'interview',
  //       component: () => import('@/views/reader/interview/index'),
  //       meta: { title: '采访', icon: 'interview1' }
  //     },
  //     {
  //       path: 'appointment',
  //       name: 'appointment',
  //       component: () => import('@/views/reader/order'),
  //       meta: { title: '预约记录', icon: 'order' }
  //     },
  //     {
  //       path: 'userRecord',
  //       name: 'userRecord',
  //       component: () => import('@/views/reader/userRecord'),
  //       meta: { title: '借阅记录', icon: 'borrow' }
  //     },
  //     {
  //       path: 'overdue',
  //       name: 'overdue',
  //       component: () => import('@/views/reader/overdue'),
  //       meta: { title: '超期通报', icon: 'overdue' }
  //     }
  //   ]
  // },

  // {
  //   path: '/circulate',
  //   component: Layout,
  //   redirect: '/circulate',
  //   name: 'circulate',
  //   meta: { title: '流通管理系统', icon: 'circulate' },
  //   children: [
  //     {
  //       path: 'borrow',
  //       name: 'borrow',
  //       component: () => import('@/views/cirManage/borrowBook'),
  //       meta: { title: '单次借书', icon: 'borrow' }
  //     },
  //     {
  //       path: 'b_order',
  //       name: 'b_order',
  //       component: () => import('@/views/cirManage/orderMan'),
  //       meta: { title: '预约管理', icon: 'order' }
  //     },
  //     {
  //       path: 'b_return',
  //       name: 'b_return',
  //       component: () => import('@/views/cirManage/borrow_return'),
  //       meta: { title: '借还管理', icon: 'return' }
  //     }
  //   ]
  // },
  // {
  //   path: '/catalogue',
  //   component: Layout,
  //   redirect: '/catalogue',
  //   name: 'catalogue',
  //   meta: { title: '编目管理系统', icon: 'catalogue' },
  //   children: [
  //     {
  //       path: 'intResult',
  //       name: 'intResult',
  //       component: () => import('@/views/catalogue/interviewResult'),
  //       meta: { title: '采访清单', icon: 'interview' }
  //     },
  //     // {
  //     //   path: 'addBook',
  //     //   name: 'addBook',
  //     //   component: () => import('@/views/catalogue/addBook'),
  //     //   meta: { title: '新增图书', icon: 'nested' }
  //     // },

  //     {
  //       path: 'catalogueBook',
  //       name: 'catalogueBook',
  //       component: () => import('@/views/catalogue/index'),
  //       meta: { title: '到馆图书处理', icon: 'newbook' }
  //     },
  //     {
  //       path: 'cataResult',
  //       name: 'cataResult',
  //       component: () => import('@/views/catalogue/cataResult'),
  //       meta: { title: '编目结果', icon: 'catalogueResult' }
  //     },
  //     {
  //       path: 'deleteBook',
  //       name: 'deleteBook',
  //       component: () => import('@/views/catalogue/deleteBook'),
  //       meta: { title: '报损图书', icon: 'loss' }
  //     },
  //     {
  //       path: 'returnResult',
  //       name: 'returnResult',
  //       component: () => import('@/views/catalogue/returnResult'),
  //       meta: { title: '退货清单', icon: 'link' }
  //     }
  //   ]
  // },
  // {
  //   path: '/userSystem',
  //   component: Layout,
  //   redirect: '/userSystem',
  //   name: 'userSystem',
  //   meta: { title: '用户管理系统', icon: 'user1' },
  //   children: [
  //     {
  //       path: 'user',
  //       name: 'user',
  //       component: () => import('@/views/user/userManagement'),
  //       meta: { title: '用户管理', icon: 'user' }
  //     }
  //   ]
  // },
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

export const asyncRouterMap = [
  // {
  //   path: '/permission',
  //   component: Layout,
  //   name: 'permission',
  //   redirect: '/permission/index222',
  //   meta: {title:'permission', role: ['0'] }, //页面需要的权限
  //   children: [
  //     { 
  //       path: 'index222',
  //       component: () => import('@/views/test/book'),
  //       name: 'index222',
  //       meta: {title:'权限测试1',role: ['0','super_editor'] }  //页面需要的权限
  //     },
  //     { 
  //       path: 'index333',
  //       component: () => import('@/views/test/borrow'),
  //       name: 'index333',
  //       meta: {title:'权限测试2',role: ['0','super_editor'] }  //页面需要的权限
  //     }
  //   ]
  // },
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
      meta: { title: '图书管理系统', icon: 'library'}
    }]
  },

  {
    path: '/reader',
    component: Layout,
    redirect: '/reader',
    name: 'reader',
    meta: { title: '读者系统', icon: 'reader' },
    children: [
      {
        path: 'book',
        name: 'book',
        component: () => import('@/views/reader/book'),
        meta: { title: '馆藏展示', icon: 'book' }
      },
      {
        path: 'interview',
        name: 'interview',
        component: () => import('@/views/reader/interview/index'),
        meta: { title: '采访', icon: 'interview1' }
      },
      {
        path: 'appointment',
        name: 'appointment',
        component: () => import('@/views/reader/order'),
        meta: { title: '预约记录', icon: 'order' }
      },
      {
        path: 'userRecord',
        name: 'userRecord',
        component: () => import('@/views/reader/userRecord'),
        meta: { title: '借阅记录', icon: 'borrow' }
      }
    ]
  },

  {
    path: '/circulate',
    component: Layout,
    redirect: '/circulate',
    name: 'circulate',
    meta: { title: '流通管理系统', icon: 'circulate',role: ['0','4']},
    children: [
      {
        path: 'borrow',
        name: 'borrow',
        component: () => import('@/views/cirManage/borrowBook'),
        meta: { title: '单次借书', icon: 'borrow' }
      },
      {
        path: 'b_order',
        name: 'b_order',
        component: () => import('@/views/cirManage/orderMan'),
        meta: { title: '预约管理', icon: 'order' }
      },
      {
        path: 'b_return',
        name: 'b_return',
        component: () => import('@/views/cirManage/borrow_return'),
        meta: { title: '借还管理', icon: 'return' }
      }
    ]
  },
  {
    path: '/catalogue',
    component: Layout,
    redirect: '/catalogue',
    name: 'catalogue',
    meta: { title: '编目管理系统', icon: 'catalogue' ,role: ['0','2','3']},
    children: [
      {
        path: 'intResult',
        name: 'intResult',
        component: () => import('@/views/catalogue/interviewResult'),
        meta: { title: '采访清单', icon: 'interview' }
      },
      // {
      //   path: 'addBook',
      //   name: 'addBook',
      //   component: () => import('@/views/catalogue/addBook'),
      //   meta: { title: '新增图书', icon: 'nested' }
      // },

      {
        path: 'catalogueBook',
        name: 'catalogueBook',
        component: () => import('@/views/catalogue/index'),
        meta: { title: '到馆图书处理', icon: 'newbook' }
      },
      {
        path: 'cataResult',
        name: 'cataResult',
        component: () => import('@/views/catalogue/cataResult'),
        meta: { title: '编目结果', icon: 'catalogueResult' }
      },
      {
        path: 'deleteBook',
        name: 'deleteBook',
        component: () => import('@/views/catalogue/deleteBook'),
        meta: { title: '报损图书', icon: 'loss' }
      },
      {
        path: 'returnResult',
        name: 'returnResult',
        component: () => import('@/views/catalogue/returnResult'),
        meta: { title: '退货清单', icon: 'link' }
      }
    ]
  },
  {
    path: '/userSystem',
    component: Layout,
    redirect: '/userSystem',
    name: 'userSystem',
    meta: { title: '用户管理系统', icon: 'user1' ,role: ['0','5']},
    children: [
      {
        path: 'user',
        name: 'user',
        component: () => import('@/views/user/userManagement'),
        meta: { title: '用户管理', icon: 'user' }
      }
    ]
  },
  { path: '*', redirect: '/404', hidden: true }
];

export default router
