import Vue from 'vue'
import App from './App.vue'
import vuetify from './plugins/vuetify';
import animated from 'animate.css'
import router from './router/router'
import store from './store/store'

Vue.use(animated)
Vue.config.productionTip = false

new Vue({
  vuetify,
  router,
  store,
  render: h => h(App)
}).$mount('#app')
