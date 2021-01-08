import router from './router'
import store from './store'
import { Message } from 'element-ui'
import NProgress from 'nprogress' // progress bar
import 'nprogress/nprogress.css' // progress bar style
import { getToken } from '@/utils/auth' // get token from cookie
import getPageTitle from '@/utils/get-page-title'
// import permission from '@/store/modules/permission'

NProgress.configure({ showSpinner: false }) // NProgress Configuration

const whiteList = ['/login'] // no redirect whitelist

router.beforeEach(async(to, from, next) => {
  // start progress bar
  NProgress.start()

  // set page title
  document.title = getPageTitle(to.meta.title)

  // determine whether the user has logged in
  
  const hasToken = getToken()
  // next({ path: '/' })
  // NProgress.done()
  if (hasToken) {
    console.log(hasToken,"token111")
    if (to.path === '/login') {
      // if is logged in, redirect to the home page
      next({ path: '/' })
      NProgress.done()
    } else {
      const hasGetUserInfo = store.getters.name
      if (hasGetUserInfo) {
        next()
      } else {
        try {
          // get user info
          // await store.dispatch('user/getInfo')
          //获取roles
          // console.log("第0步")
          // const { user_role } = await store.dispatch('user/getInfo')//第一步
          // console.log(user_role,"第1步")
          // //获取通过权限验证的路由
          // const accessRoutes = this.$store.dispatch('permission/GenerateRoutes', user_role)//第二步
          // console.log("第2步")

          // //更新加载路由
          // router.options.routes = store.getters.permission_routes//第三步
          // console.log("第3步")
          // router.addRoutes(accessRoutes)
          //第二种
          // const roles=store.getters.roles;
          const  user_role  = await store.dispatch('user/getInfo')
          console.log(user_role,'第二种测试')
          store.dispatch('permission/GenerateRoutes',  user_role ).then((pages) => { // 生成可访问的路由表
            console.log(store.getters.permission_routes,store.getters.name,"per动态路由添加的路由")
            console.log(pages,"pages")
            router.addRoutes(pages); // 动态添加可访问路由表
            router.options.routes=pages;
            next({ ...to, replace: true });// hack方法 确保addRoutes已完成 ,set the replace: true so the navigation will not leave a history record
          })
          next()
        } catch (error) {
          // remove token and go to login page to re-login
          await store.dispatch('user/resetToken')
          // Message.error(error || 'Has Error')
          Message.error('Has Error')
          next(`/login?redirect=${to.path}`)
          NProgress.done()
        }
      }
    }
  } else {
    /* has no token*/
    console.log("zheli")
    if (whiteList.indexOf(to.path) !== -1) {
      // in the free login whitelist, go directly
      next()
    } else {
      // other pages that do not have permission to access are redirected to the login page.
      next(`/login?redirect=${to.path}`)
      NProgress.done()
    }
  }
})

router.afterEach(() => {
  // finish progress bar
  NProgress.done()
})

