<template>
  <section class="container mx-auto">
    <div class="w-full rounded-lg">
      <div class="w-full overflow-x-auto">
        <h1 class="text-xl text-gray-900 font-semibold mt-3">
          {{ user.username }}'s profile
        </h1>
        <div class="rounded-xl bg-white overflow-hidden bg-opacity-50">
          <table
            class="w-full border rounded shadow-md rounded-2xl bg-opacity-0"
          >
            <thead>
              <tr class="text-left text-gray-900 bg-blue-500">
                <th class="text-gray-50 px-4 py-3">User</th>
                <th class="text-gray-50 px-4 py-3">Created</th>
                <th class="text-gray-50 px-4 py-3">Rating</th>
                <th class="text-gray-50 px-4 py-3">Status</th>
              </tr>
            </thead>
            <tbody class="bg-white">
              <tr class="text-gray-700">
                <td class="px-4 py-3">
                  <div class="flex items-center text-sm">
                    <div class="relative w-8 h-8 mr-3 rounded-full md:block">
                      <img
                        class="object-cover w-full h-full rounded-full"
                        src="https://placekitten.com/160/160"
                        alt=""
                        loading="lazy"
                      />
                      <div
                        class="absolute inset-0 rounded-full shadow-inner"
                        aria-hidden="true"
                      ></div>
                    </div>
                    <div>
                      <NuxtLink
                        class="font-semibold text-black hover:underline"
                        :to="{ name: 'users-id', params: { id: user.id } }"
                      >
                        <span>
                          {{ user.username }}
                        </span>
                      </NuxtLink>
                      <p class="text-xs text-gray-600">{{ user.role }}</p>
                    </div>
                  </div>
                </td>
                <td class="px-4 py-3 text-sm">{{ user.created }}</td>
                <td class="px-4 py-3 text-sm">{{ user.rating }}</td>
                <td class="px-4 py-3 text-xs">
                  <span
                    v-if="user.status"
                    class="
                      px-2
                      py-1
                      font-semibold
                      leading-tight
                      text-green-700
                      bg-green-100
                      rounded-sm
                    "
                  >
                    Online
                  </span>
                  <span
                    v-else
                    class="
                      px-2
                      py-1
                      font-semibold
                      leading-tight
                      text-gray-700
                      bg-gray-100
                      rounded-sm
                    "
                  >
                    Offline
                  </span>
                </td>
              </tr>
            </tbody>
          </table>
        </div>
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
