<template>
  <v-container>
    <v-card class="pa-6 mx-auto" max-width="400">
      <v-card-title>ログイン</v-card-title>
      <v-card-text>
        <v-form @submit.prevent="handleLogin">
          <v-text-field v-model="username" label="ユーザー名" required />
          <v-text-field v-model="password" label="パスワード" type="password" required />
          <v-btn type="submit" block color="primary">ログイン</v-btn>
        </v-form>
        <p v-if="error" class="text-error mt-2">{{ error }}</p>
      </v-card-text>
    </v-card>
  </v-container>
</template>

<script setup>
import { ref } from "vue";
import { useAuthStore } from "../store";
import { login, authStatus } from "../api/auth";

const username = ref("");
const password = ref("");
const error = ref("");

const authStore = useAuthStore();

async function handleLogin() {
  try {
    await login(username.value, password.value);
    const res = await authStatus();
    authStore.setUser(res.data);
    alert("ログイン成功: " + res.data.username);
  } catch (err) {
    error.value = "ログイン失敗";
  }
}
</script>