

const routes=[
    {path:'/home',component:home},
    {path:'/teacher',component:teacher},
    {path:'/group',component:group},
    {path:'/classroom',component:classroom},
    {path:'/department',component:department},
    {path:'/auditory',component:auditory}
]

const router = VueRouter.createRouter({
    // 4. Provide the history implementation to use. We are using the hash history for simplicity here.
    history: VueRouter.createWebHashHistory(),
    routes, // short for `routes: routes`
  })
  
  // 5. Create and mount the root instance.
  const app = Vue.createApp({})
  // Make sure to _use_ the router instance to make the
  // whole app router-aware.
  app.use(router)
  
  app.mount('#app')