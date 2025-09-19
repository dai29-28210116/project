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
import { useRouter } from "vue-router";
import { useAuthStore } from "../store/auth";
import { useUiStore } from "../store/ui";
import { login, authStatus } from "../api/auth";

const router = useRouter();
const authStore = useAuthStore();
const ui = useUiStore();

const username = ref("");
const password = ref("");
const error = ref("");

async function handleLogin() {
  try {
    await login(username.value, password.value);
    const res = await authStatus();
    authStore.setUser(res.data);
    ui.showSnackbar("ログイン成功: " + res.data.username, "success");
    router.push("/");
  } catch (err) {
    ui.showSnackbar("ログイン失敗", "error");
    error.value = "ログイン失敗";
  }
}
</script>
