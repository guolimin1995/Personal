import Vue from 'vue'
import Router from 'vue-router'
import Index from '../views/Index.vue'

Vue.use(Router)

export default new Router({
    mode: 'history',
    base: process.env.BASE_URL,
    routes: [
        {
            path: '/',
            name: 'index',
            component: Index,
            children: [

            ]
        },
        {
            path: '/article',
            name: 'article',
            component: () => import('@/views/Article/Article'),
        },
        {
            path: '/about',
            name: 'about',
            component: () => import('@/views/About/About'),
        },
    ]
})