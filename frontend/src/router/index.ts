import { createRouter, createWebHistory } from 'vue-router'

import Dashboard from '@/views/Dashboard.vue'
const Vessel = () => import('@/views/vessel/index.vue')
const Berth = () => import('@/views/berth/index.vue')
const Crane = () => import('@/views/crane/index.vue')
const Yard = () => import('@/views/yard/index.vue')
const Container = () => import('@/views/container/index.vue')
const Gate = () => import('@/views/gate/index.vue')
const Yc = () => import('@/views/yc/index.vue')
const Danger = () => import('@/views/danger/index.vue')
const Tally = () => import('@/views/tally/index.vue')
const Customs = () => import('@/views/customs/index.vue')
const Truck = () => import('@/views/truck/index.vue')
const Barge = () => import('@/views/barge/index.vue')
const Reefer = () => import('@/views/reefer/index.vue')
const Repair = () => import('@/views/repair/index.vue')
const Rail = () => import('@/views/rail/index.vue')
const ShippingLine = () => import('@/views/shipping_line/index.vue')
const EquipMaintain = () => import('@/views/equip_maintain/index.vue')
const Dispatch = () => import('@/views/dispatch/index.vue')

const router = createRouter({
  history: createWebHistory(),
  routes: [
    { path: '/', name: 'dashboard', component: Dashboard },
    { path: '/vessel', name: 'vessel', component: Vessel },
    { path: '/berth', name: 'berth', component: Berth },
    { path: '/crane', name: 'crane', component: Crane },
    { path: '/yard', name: 'yard', component: Yard },
    { path: '/container', name: 'container', component: Container },
    { path: '/gate', name: 'gate', component: Gate },
    { path: '/yc', name: 'yc', component: Yc },
    { path: '/danger', name: 'danger', component: Danger },
    { path: '/tally', name: 'tally', component: Tally },
    { path: '/customs', name: 'customs', component: Customs },
    { path: '/truck', name: 'truck', component: Truck },
    { path: '/barge', name: 'barge', component: Barge },
    { path: '/reefer', name: 'reefer', component: Reefer },
    { path: '/repair', name: 'repair', component: Repair },
    { path: '/rail', name: 'rail', component: Rail },
    { path: '/shipping_line', name: 'shipping_line', component: ShippingLine },
    { path: '/equip_maintain', name: 'equip_maintain', component: EquipMaintain },
    { path: '/dispatch', name: 'dispatch', component: Dispatch },
  ],
})

export default router
