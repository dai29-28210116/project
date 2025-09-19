<template>
  <v-dialog v-model="dialog" max-width="700">
    <v-card>
      <v-card-title>
        {{ notice?.id ? "お知らせ詳細" : "新規お知らせ" }}
      </v-card-title>
      <v-card-text>
        <div v-if="notice">
          <h3>{{ notice.title }}</h3>
          <div v-html="notice.content"></div>
        </div>
        <div v-else>
          <p>ここに新規登録フォームを作成予定</p>
        </div>
      </v-card-text>
      <v-card-actions>
        <v-spacer />
        <v-btn text @click="dialog = false">閉じる</v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>

<script setup>
const dialog = defineModel({ type: Boolean }); // 親の v-model と同期
defineProps({
  notice: Object,
});
defineEmits(["saved"]);
</script>
