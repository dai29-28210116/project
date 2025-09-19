
<template>
  <v-dialog v-model="modelValue" max-width="400">
    <v-card>
      <v-card-title>カテゴリ管理</v-card-title>
      <v-card-text>
        <p>カテゴリの登録・編集機能をここに実装予定</p>
      </v-card-text>
      <v-card-actions>
        <v-spacer />
        <v-btn text @click="modelValue = false">閉じる</v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>
<script setup>
const modelValue = defineModel({ type: Boolean });
</script>
