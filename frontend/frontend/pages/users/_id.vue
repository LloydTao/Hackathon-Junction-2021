<template>
  <div class="bg-blue-100">
    <div class="flex flex-col container mx-auto px-5 py-5">
      <UsersDetail />
      <div class="mt-8" />
      <MessagesList />
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      id: this.$route.params.id,
    }
  },
}
</script>
