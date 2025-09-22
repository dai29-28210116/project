<!-- src/components/notice/NoticeDialog.vue -->
<template>
  <v-dialog v-model="dialog" max-width="800">
    <v-card>
      <v-card-title>
        {{ notice?.id ? "お知らせ編集" : "新規お知らせ" }}
      </v-card-title>
      <v-card-text>
        <v-form>
          <v-text-field v-model="form.title" label="タイトル" />

          <!-- QuillEditor 本文入力 -->
          <label class="mb-2">本文</label>
          <QuillEditor
            v-model:content="form.content"
            content-type="html"
            theme="snow"
            style="height: 300px"
          />

          <!-- 公開期間 -->
          <v-row class="mt-4">
            <v-col>
              <v-text-field v-model="form.publish_from" label="公開開始日" type="date" />
            </v-col>
            <v-col>
              <v-text-field v-model="form.publish_to" label="公開終了日" type="date" />
            </v-col>
          </v-row>

          <!-- 部署選択 -->
          <v-select
            v-model="form.departments"
            :items="departments"
            item-title="name"
            item-value="id"
            label="対象部署"
            multiple
            chips
          />

          <!-- カテゴリ選択 -->
          <v-select
            v-model="form.categories"
            :items="categories"
            item-title="name"
            item-value="id"
            label="カテゴリ"
            multiple
            chips
          />

          <!-- 添付ファイル -->
          <div class="mt-4">
            <h4>添付ファイル</h4>
            <AttachmentUploader
              v-if="notice?.id && noticeContentTypeId"
              :contentType="noticeContentTypeId" 
              :objectId="notice.id"
              section="main"
              :isEditMode="true"
            />
            <div v-else class="text-grey text-caption">
              保存後にファイルを添付できます
            </div>
          </div>

        </v-form>
      </v-card-text>
      <v-card-actions>
        <v-spacer />
        <v-btn text @click="dialog = false">キャンセル</v-btn>
        <v-btn color="primary" @click="saveNotice">保存</v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>

<script setup>
import { ref, watch, onMounted } from "vue";
import { QuillEditor } from "@vueup/vue-quill";
import "@vueup/vue-quill/dist/vue-quill.snow.css";

// 共通コンポーネント
import AttachmentUploader from "@/components/core/AttachmentUploader.vue";

// API モジュール
import { createNotice, updateNotice, fetchCategories } from "../../api/notice";
import { fetchDepartments } from "../../api/dept";
import apiClient from "../../api/axios"; // ← apiClient を利用

const dialog = defineModel({ type: Boolean });
const props = defineProps({ notice: Object });
const emit = defineEmits(["saved"]);

const form = ref({
  title: "",
  content: "",
  publish_from: "",
  publish_to: "",
  departments: [],
  categories: [],
});

const departments = ref([]);
const categories = ref([]);
const noticeContentTypeId = ref(null);

// マスタロード
const loadMasters = async () => {
  const deptRes = await fetchDepartments();
  departments.value = deptRes.data;
  const catRes = await fetchCategories();
  categories.value = catRes.data;
};

// ContentType ID の取得
const fetchContentTypeId = async () => {
  try {
    const res = await apiClient.get("core/content-types/", {
      params: { model: "notice" },
    });
    if (res.data?.length) {
      noticeContentTypeId.value = res.data[0].id;
    }
  } catch (err) {
    console.error("contentTypeId取得失敗", err);
  }
};

watch(
  () => props.notice,
  (val) => {
    if (val) {
      form.value = {
        ...val,
        departments: val.departments.map((d) => d.id),
        categories: val.categories.map((c) => c.id),
      };
    } else {
      form.value = {
        title: "",
        content: "",
        publish_from: "",
        publish_to: "",
        departments: [],
        categories: [],
      };
    }
  },
  { immediate: true }
);

onMounted(() => {
  loadMasters();
  fetchContentTypeId();
});

const saveNotice = async () => {
  const payload = {
    title: form.value.title,
    content: form.value.content,
    publish_from: form.value.publish_from,
    publish_to: form.value.publish_to,
    department_ids: form.value.departments,
    category_ids: form.value.categories,
  };

  if (props.notice?.id) {
    await updateNotice(props.notice.id, payload);
  } else {
    await createNotice(payload);
  }
  emit("saved");
  dialog.value = false;
};
</script>


<style scoped>
.info-text {
  font-size: 0.85rem;
  color: #555;
  padding: 8px 0;
}
</style>
