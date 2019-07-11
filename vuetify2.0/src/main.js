import Vue from 'vue'
import App from './App.vue'
import vuetify from './plugins/vuetify';
import animated from 'animate.css'

Vue.use(animated)
Vue.config.productionTip = false

new Vue({
  vuetify,
  render: h => h(App)
}).$mount('#app')
