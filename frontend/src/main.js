// src/main.js
import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";
import { createPinia } from "pinia";

// Vuetify 読み込み
import vuetify from "./plugins/vuetify";
import "vuetify/styles";              
import "@mdi/font/css/materialdesignicons.css"; // アイコン

const app = createApp(App);

app.use(router);
app.use(createPinia());
app.use(vuetify);

app.mount("#app");
