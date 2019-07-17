import Vue from 'vue'
import App from './App.vue'
import vuetify from './plugins/vuetify';
import animated from 'animate.css'
import router from './router/router'

Vue.use(animated)
Vue.config.productionTip = false

new Vue({
  vuetify,
  router,
  render: h => h(App)
}).$mount('#app')
