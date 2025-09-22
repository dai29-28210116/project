<template>
  <div>
    <!-- 編集モード時のみファイル追加表示 -->
    <v-file-input
      v-if="isEditMode"
      :label="label"
      multiple
      show-size
      @change="handleUpload"
      :prepend-icon="icon"
    />

    <!-- ファイル一覧表示は常に出す -->
    <div class="attachment-container">
      <div
        class="attachment-item"
        v-for="file in files"
        :key="file.id"
      >
        <div class="file-row">
          <template v-if="isImage(file.file)">
            <a :href="file.file" target="_blank" rel="noopener noreferrer">
              <img
                :src="file.file"
                class="thumbnail"
                :alt="file.original_filename"
              />
            </a>
          </template>
          <template v-else>
            <a :href="file.file" target="_blank" class="file-link">
              {{ file.original_filename }}
            </a>
          </template>

          <!-- 編集モード時のみ削除ボタン -->
          <v-btn
            v-if="isEditMode"
            icon
            size="x-small"
            variant="text"
            color="red"
            @click="deleteFile(file.id)"
          >
            <v-icon size="24">mdi-delete</v-icon>
          </v-btn>
        </div>

        <div class="file-meta">
          <small class="text-grey">{{ file.original_filename }}</small>
          <small class="text-grey">{{ formatDate(file.uploaded_at) }}</small>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import {
  fetchAttachments,
  uploadAttachment,
  deleteAttachment,
} from "@/api/attachment";

export default {
  props: {
    contentType: { type: Number, required: true }, // ← 数値IDを渡す
    objectId: { type: Number, required: true },    // Notice の id
    section: { type: String, default: "main" },    // 添付対象セクション
    isEditMode: { type: Boolean, default: false },
    label: { type: String, default: "添付ファイルを選択" },
    icon: { type: String, default: "mdi-paperclip" },
  },
  data() {
    return {
      files: [],
    };
  },
  mounted() {
    this.loadFiles();
  },
  methods: {
    async loadFiles() {
      if (!this.objectId) return;
      try {
       const res = await fetchAttachments({
         content_type_id: this.contentType, 
         object_id: this.objectId,
         section: this.section,
        });
        this.files = res.data;
      } catch (err) {
        console.error("[ERROR] loadFiles failed:", err);
      }
    },
    async handleUpload(event) {
      if (!this.objectId) {
        console.error("[ERROR] objectId is null");
        return;
      }
      const files = Array.from(event.target?.files || event);
      for (const file of files) {
        await uploadAttachment(file, this.contentType, this.objectId, this.section);
      }
      this.loadFiles();
    },
    async deleteFile(id) {
      const confirmed = window.confirm("このファイルを削除しますか？");
      if (!confirmed) return;
      try {
        await deleteAttachment(id);
        this.loadFiles();
      } catch (err) {
        console.error("[ERROR] deleteFile failed:", err);
      }
    },
    isImage(fileUrl) {
      return /\.(jpe?g|png|gif|bmp|webp)$/i.test(fileUrl);
    },
    formatDate(dateStr) {
      if (!dateStr) return "";
      return new Date(dateStr).toLocaleString();
    },
  },
};
</script>

<style scoped>
.attachment-container {
  display: flex;
  flex-wrap: wrap;
  gap: 16px;
  margin-top: 12px;
}
.attachment-item {
  position: relative;
  width: 140px;
  padding: 8px;
  border-radius: 6px;
  background: #f9f9f9;
  display: flex;
  flex-direction: column;
  align-items: center;
  box-shadow: 0 0 2px rgba(0, 0, 0, 0.05);
  transition: transform 0.2s ease;
}
.thumbnail {
  width: 100%;
  height: auto;
  border-radius: 4px;
  transition: transform 0.2s ease;
  object-fit: contain;
  max-height: 100px;
  z-index: 1;
  position: relative;
}
.attachment-item:hover .thumbnail {
  transform: scale(1.8);
  z-index: 1;
}
.v-btn {
  z-index: 2;
  position: relative;
}
.file-row {
  display: flex;
  justify-content: space-between;
  align-items: center;
  width: 100%;
}
.file-link {
  color: #1976d2;
  font-weight: bold;
  text-decoration: none;
  max-width: 100%;
  word-break: break-word;
}
.file-meta {
  margin-top: 4px;
  text-align: center;
  font-size: 0.75rem;
}
</style>
