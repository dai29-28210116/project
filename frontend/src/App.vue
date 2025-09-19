<template>
  <v-app>
    <v-app-bar app color="primary" dark>
      <v-app-bar-nav-icon @click="drawer = !drawer" />
      <v-toolbar-title>業務システム</v-toolbar-title>

      <v-spacer />

      <!-- ユーザー名と部署表示 -->
      <div v-if="authStore.user" class="d-flex align-center mr-4" style="gap: 8px;">
        <span>ようこそ {{ authStore.user.full_name }} さん</span>
        <v-chip color="white" text-color="primary" size="small" variant="outlined">
          {{ currentDeptName }}
        </v-chip>
      </div>

      <!-- ログイン/ログアウトボタン -->
      <v-btn v-if="authStore.user" @click="handleLogout" icon>
        <v-icon>mdi-logout</v-icon>
      </v-btn>
      <v-btn v-else to="/login" icon>
        <v-icon>mdi-login</v-icon>
      </v-btn>
    </v-app-bar>

    <v-navigation-drawer v-model="drawer" app>
      <v-list>
        <template v-for="menu in menus" :key="menu.code">
          <!-- 子メニューを持つ場合 -->
          <v-list-group
            v-if="menu.children && menu.children.length"
            :prepend-icon="menu.icon || 'mdi-folder'"
          >
            <template #activator="{ props }">
              <v-list-item v-bind="props">
                <v-list-item-title>{{ menu.title }}</v-list-item-title>
              </v-list-item>
            </template>

            <!-- 2階層目 -->
            <v-list-item
              v-for="child in menu.children"
              :key="child.code"
              :to="child.path"
              link
            >
              <v-list-item-title>{{ child.title }}</v-list-item-title>
            </v-list-item>
          </v-list-group>

          <!-- 子メニューを持たない場合 -->
          <v-list-item v-else :to="menu.path" link>
            <v-list-item-title>{{ menu.title }}</v-list-item-title>
          </v-list-item>
        </template>
      </v-list>
    </v-navigation-drawer>

    <v-main>
      <router-view />
    </v-main>

    <CommonSnackbar />
  </v-app>
</template>

<script setup>
import { ref, onMounted, computed } from "vue";
import { useAuthStore } from "./store/auth";
import { useUiStore } from "./store/ui";
import { logout, authStatus } from "./api/auth";
import { fetchMenus } from "./api/menu";
import CommonSnackbar from "./components/CommonSnackbar.vue";

const drawer = ref(false);
const menus = ref([]);
const authStore = useAuthStore();
const ui = useUiStore();

// 選択中の部署コード
const selectedDept = ref(null);

// 部署名を表示用に算出
const currentDeptName = computed(() => {
  if (!authStore.departments?.length) return "";
  const dept = authStore.departments.find(d => d.code === selectedDept.value);
  return dept ? dept.name : authStore.departments[0].name;
});

async function handleLogout() {
  await logout();
  authStore.clearUser();
  ui.showSnackbar("ログアウトしました", "info");
  window.location.href = "/login";
}

onMounted(async () => {
  if (!authStore.user) {   // すでにログイン処理で user がセット済みなら呼ばない
    try {
      const res = await authStatus();
      authStore.setUser(res.data);

      if (authStore.departments?.length > 0) {
        selectedDept.value = authStore.departments[0].code;
      }
    } catch {
      authStore.clearUser();
    }
  }

  // メニューを取得
  const menuRes = await fetchMenus();
  menus.value = menuRes.data;
});

</script>
