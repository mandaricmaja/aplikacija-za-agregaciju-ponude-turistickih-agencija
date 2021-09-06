import Vue from 'vue'
import App from './App.vue'
import router from './router'
import 'bootstrap/dist/css/bootstrap.min.css'
import JwPagination from 'jw-vue-pagination';
import { BootstrapVue, BootstrapVueIcons } from 'bootstrap-vue'
import "bootstrap-icons/font/bootstrap-icons.css";
Vue.component('jw-pagination', JwPagination);
Vue.use(BootstrapVue);
Vue.use(BootstrapVueIcons);

new Vue({
  router,
  render: h => h(App)
}).$mount('#app')
