<template>
  <div>
    <h1>PROFILE</h1>
    <pre>{{ user }}</pre>
  </div>
</template>

<script>
export default {
  setup() {
    return {
      user: window.localStorage.getItem("user"),
    };
  },
};
</script>

<style lang="scss" scoped></style>
