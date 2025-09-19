<template>
  <v-container>
    <!-- 検索と新規登録 -->
    <v-row class="my-4">
      <!-- 検索ボックス -->
      <v-col cols="12" sm="6">
        <v-text-field
          v-model="keyword"
          label="検索"
          prepend-inner-icon="mdi-magnify"
          clearable
          density="compact"
          hide-details
        />
      </v-col>

      <!-- 新規登録ボタン（roles に notice_manager が含まれている場合のみ表示） -->
      <v-col cols="auto" v-if="authStore.user && authStore.user.roles?.includes('notice_manager')">
        <v-btn color="primary" @click="openCreateDialog">
          <v-icon start>mdi-plus</v-icon>
          新規登録
        </v-btn>
      </v-col>
    </v-row>

    <!-- 表示切替 -->
    <v-btn-toggle v-model="viewMode" class="mb-4">
      <v-btn value="card">カード表示</v-btn>
      <v-btn value="table">一覧表示</v-btn>
    </v-btn-toggle>

    <!-- お知らせ一覧（カード） -->
    <div v-if="viewMode === 'card'">
      <v-row>
        <v-col
          v-for="notice in notices"
          :key="notice.id"
          cols="12"
          md="6"
          lg="4"
        >
          <v-card @click="openDetailDialog(notice)">
            <v-img
              v-if="notice.attachments && notice.attachments.length"
              :src="notice.attachments[0].file"
              height="150px"
              cover
            />
            <v-card-title>{{ notice.title }}</v-card-title>
            <v-card-subtitle>
              {{ formatDate(notice.publish_from) }} ~
              {{ formatDate(notice.publish_to) }}
            </v-card-subtitle>
            <v-card-text>
              <div v-html="truncateContent(notice.content)"></div>
              <v-btn
                v-if="isTruncated(notice.content)"
                text
                @click.stop="showFull(notice)"
              >
                More
              </v-btn>
            </v-card-text>
            <v-card-actions>
              <v-chip
                v-for="cat in notice.categories"
                :key="cat.id"
                size="small"
                class="ma-1"
                color="primary"
                variant="tonal"
              >
                {{ cat.name }}
              </v-chip>
            </v-card-actions>
          </v-card>
        </v-col>
      </v-row>
    </div>

    <!-- お知らせ一覧（テーブル） -->
    <div v-else>
      <v-data-table
        :headers="headers"
        :items="notices"
        @click:row="openDetailDialog"
      >
        <template #item.attachments="{ item }">
          <div v-if="item.attachments?.length">
            <a
              v-for="att in item.attachments"
              :key="att.id"
              :href="att.file"
              target="_blank"
            >
              {{ att.original_name }}
            </a>
          </div>
        </template>
        <template #item.content="{ item }">
          <div v-html="shorten(item.content, 30)"></div>
        </template>
      </v-data-table>
    </div>

    <!-- 詳細 / 新規登録ダイアログ -->
    <NoticeDialog
      v-model="dialog"
      :notice="selectedNotice"
      @saved="loadNotices"
    />

    <!-- カテゴリ編集用ダイアログ -->
    <CategoryDialog v-model="categoryDialog" @saved="loadCategories" />
  </v-container>
</template>

<script setup>
import { ref, onMounted } from "vue";
import { useAuthStore } from "../store/auth";
import { fetchNotices } from "../api/notice";
import NoticeDialog from "../components/notice/NoticeDialog.vue";
import CategoryDialog from "../components/notice/CategoryDialog.vue";

const authStore = useAuthStore();

const notices = ref([]);
const keyword = ref("");
const viewMode = ref("card");
const dialog = ref(false);
const selectedNotice = ref(null);
const categoryDialog = ref(false);

const headers = [
  { title: "タイトル", key: "title" },
  { title: "期間", key: "publish_from" },
  { title: "カテゴリ", key: "categories" },
  { title: "添付", key: "attachments" },
  { title: "本文", key: "content" },
];

function formatDate(dateStr) {
  return new Date(dateStr).toLocaleDateString();
}

function truncateContent(content) {
  const text = content.replace(/<[^>]+>/g, "");
  return text.length > 50 ? text.slice(0, 50) + "..." : text;
}

function isTruncated(content) {
  const text = content.replace(/<[^>]+>/g, "");
  return text.length > 50;
}

function showFull(notice) {
  selectedNotice.value = notice;
  dialog.value = true;
}

function shorten(content, len) {
  const text = content.replace(/<[^>]+>/g, "");
  return text.length > len ? text.slice(0, len) + "..." : text;
}

async function loadNotices() {
  const res = await fetchNotices({ search: keyword.value });
  notices.value = res.data;
}

function openDetailDialog(notice) {
  selectedNotice.value = notice;
  dialog.value = true;
}

function openCreateDialog() {
  selectedNotice.value = null;
  dialog.value = true;
}

onMounted(() => {
  loadNotices();
});
</script>
