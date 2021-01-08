import { asyncRouterMap, constantRoutes } from '@/router';

// function hasPermission(roles, route) {
//     console.log(roles, route, "动态路由测试");
//     let my_roles = [];
//     my_roles.push(String(roles.user_role));
//     if (route.meta && route.meta.role) {
//         console.log(my_roles, "动态路由测试2");
//         // return my_roles.some(role => route.meta.role.indexOf(role) >= 0)
//         let test = my_roles.some(role => route.meta.role.indexOf(role) >= 0)
//         console.log(test)
//         return test
//     } else {
//         return true
//     }
// }
function hasPermission(roles, route) {
    console.log(route, "动态路由测试_页面")
    let my_roles = String(roles);
    // my_roles.push(String(roles));
    console.log(my_roles,typeof(my_roles), "动态路由测试_角色")
    if (route.meta && route.meta.role) {
        console.log( route.meta.role,"动态路由测试_拥有页面权限的角色")
        let test = route.meta.role.indexOf(my_roles)>=0
        console.log(test,"动态路由测试_检查结果")
        // return my_roles.some(role => route.meta.role.indexOf(role) >= 0)
        return route.meta.role.indexOf(my_roles)>=0
    } else {
        return true
    }
}

const permission = {
    namespaced: true,
    state: {
        routers: constantRoutes,
        addRouters: []
    },
    mutations: {
        SET_ROUTERS: (state, routers) => {
            state.permission_routes = routers;
            console.log(state.permission_routes,"set_pre")
            state.routers = constantRoutes.concat(routers);
        }
    },
    actions: {
        GenerateRoutes({ commit }, data) {//roles是用户所带的权限
            console.log("动态路由", data)
            return new Promise(resolve => {
                const roles = data.user_role;
                console.log(data.user_role, roles, "动态路由测试1");
                const accessedRouters = asyncRouterMap.filter(v => {
                    // if (roles.indexOf('admin') >= 0) {
                    //     return true;
                    // };
                    if (hasPermission(roles, v)) {
                        if (v.children && v.children.length > 0) {
                            v.children = v.children.filter(child => {
                                if (hasPermission(roles, child)) {
                                    return child
                                }
                                return false;
                            });
                            return v
                        } else {
                            return v
                        }
                    }
                    return false;
                });
                console.log(accessedRouters,"动态路由筛选结果")
                commit('SET_ROUTERS', accessedRouters);
                resolve(accessedRouters);
            })
        }
    }
};

export default permission;