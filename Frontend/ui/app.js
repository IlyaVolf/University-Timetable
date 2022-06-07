

const routes=[
    {path:'/home',component:home},
    {path:'/auditory',component:auditory},
    {path:'/constraints',component:constraints},
    {path:'/ep',component:ep},
    //{path:'/faculty',component:faculty},
    {path:'/group',component:group},
    {path:'/subject',component:subject},
    {path:'/teacher',component:teacher},
    {path:'/schedule',component:schedule},
    {path:'/department',component:department},
    
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