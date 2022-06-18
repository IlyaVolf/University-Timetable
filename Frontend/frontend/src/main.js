import Vue from "vue";
import App from "./App.vue";
import "bootstrap/dist/css/bootstrap.css";
import router from "./router";
import BootstrapVue from "bootstrap-vue";
import VueSimpleAlert from "vue-simple-alert";

Vue.use(VueSimpleAlert);

Vue.config.productionTip = false;
Vue.use(BootstrapVue)

new Vue({
  router,
  render: (h) => h(App),
}).$mount("#app");
