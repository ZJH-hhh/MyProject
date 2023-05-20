<template>
  <router-view :key="$route.fullPath" />
</template>

<script>
// 在根组件引入 bootstrap
import 'bootstrap/dist/css/bootstrap.css';
import 'bootstrap/dist/js/bootstrap';

export default {
  name: "App",
  components: {
  }
}
</script>

<style scoped></style>
