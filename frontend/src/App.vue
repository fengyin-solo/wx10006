<template>
  <div class="app-shell">
    <aside class="app-side">
      <h1 class="app-title">港口集装箱作业管理平台</h1>
      <nav class="nav-list">
        <RouterLink v-for="item in navItems" :key="item.path" :to="item.path" class="nav-item">
          {{ item.label }}
        </RouterLink>
      </nav>
    </aside>
    <main class="app-main">
      <header class="app-head">
        <span class="head-desc">面向集装箱码头的船舶靠泊、岸桥调度、堆场规划、闸口管控、危品管理、理货作业与通关协同的综合作业管理后台。</span>
        <span class="head-user">当前值班：{{ store.operator }} · {{ store.shiftLabel }}</span>
      </header>
      <RouterView />
    </main>
  </div>
</template>

<script setup lang="ts">
import { useSessionStore } from '@/stores/session'

const store = useSessionStore()

const navItems = [{ label: "运营概览", path: "/" }, { label: "船舶靠泊", path: "/vessel" }, { label: "泊位管理", path: "/berth" }, { label: "岸桥调度", path: "/crane" }, { label: "堆场规划", path: "/yard" }, { label: "集装箱管理", path: "/container" }, { label: "闸口管理", path: "/gate" }, { label: "场桥管理", path: "/yc" }, { label: "危险品管理", path: "/danger" }, { label: "理货作业", path: "/tally" }, { label: "海关查验", path: "/customs" }, { label: "外集卡管理", path: "/truck" }, { label: "支线驳船", path: "/barge" }, { label: "冷藏箱管理", path: "/reefer" }, { label: "箱体修理", path: "/repair" }, { label: "铁路集疏", path: "/rail" }, { label: "船公司对接", path: "/shipping_line" }, { label: "设备维保", path: "/equip_maintain" }, { label: "调度指令", path: "/dispatch" }]
</script>
