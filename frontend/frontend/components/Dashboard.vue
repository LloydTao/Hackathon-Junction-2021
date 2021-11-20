<template>
  <section class="container mx-auto">
    <div class="w-full rounded-lg">
      <div class="w-full overflow-x-auto">
        <h1 class="text-3xl text-gray-900 font-semibold mt-5">Dashboard</h1>
        <h1 class="text-xl font-semibold mt-5">Statistics 📊</h1>
        <DashboardCards />
        <h1 class="text-xl font-semibold mt-5">Default chat 💬</h1>
        <DashboardChat />
      </div>
    </div>
  </section>
</template>

<script>
export default {
  data() {
    return {
      user: {
        id: 1,
        username: 'lloydtao',
        role: 'Player',
        created: '2021-11-16',
        rating: 1000,
        status: 1,
      },
    }
  },
}
</script>
