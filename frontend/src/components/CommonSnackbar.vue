<template>
  <v-snackbar v-model="ui.snackbar.show" :color="ui.snackbar.color" timeout="3000">
    {{ ui.snackbar.text }}
  </v-snackbar>
</template>

<script setup>
import { useUiStore } from "../store/ui";
const ui = useUiStore();
</script>
