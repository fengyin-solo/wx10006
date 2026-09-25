# 港口集装箱作业管理平台

面向集装箱码头的船舶靠泊、岸桥调度、堆场规划、闸口管控、危品管理、理货作业与通关协同的综合作业管理后台。

这是一个前后端分离的管理平台：前端 Vue 3 + Vite + TypeScript，后端 FastAPI（Python）。
两边各自独立启动，前端 dev server 已关掉自动打开页面，启动后按终端打印的地址手工打开。

## 目录结构

```text
.
├── frontend/                 Vue 3 + Vite + TypeScript 前端
│   ├── src/views/            每个业务模块一个页面
│   ├── src/api/              统一请求封装
│   ├── src/stores/           会话与筛选状态
│   └── vite.config.ts        dev server 配置（open: false）
├── backend/                  FastAPI（Python） 后端
│   ├── app/routers/          每个业务模块一组接口
│   ├── app/services/         业务规则与状态流转
│   └── app/store.py          内存数据仓库与示例数据
├── .gitignore
└── docker-compose.yml
```

## 启动

### 后端

```bash
cd backend
python3 -m venv .venv && .venv/bin/pip install -r requirements.txt
./run.sh
```

健康检查：`curl http://127.0.0.1:8000/api/health`

### 前端

```bash
cd frontend
npm install
npm run dev
```

前端默认监听 `http://127.0.0.1:5173/`，dev server 不会自动打开浏览器，
需要自己访问。`/api` 由 vite 代理到后端 `http://127.0.0.1:8000`。

## 业务模块

| 模块 | 目录 | 业务对象 | 主要字段 |
| --- | --- | --- | --- |
| 船舶靠泊 | `vessel` | 船舶 | 船舶编号、船名、航次号 |
| 泊位管理 | `berth` | 码头泊位 | 泊位编号、泊位名称、靠泊能力 |
| 岸桥调度 | `crane` | 岸桥 | 岸桥编号、所在泊位、吊具类型 |
| 堆场规划 | `yard` | 堆场贝位 | 贝位编号、所属堆场、箱区类型 |
| 集装箱管理 | `container` | 集装箱 | 箱号、箱型尺寸、箱公司 |
| 闸口管理 | `gate` | 进出记录 | 记录编号、箱号、车牌号 |
| 场桥管理 | `yc` | 场桥 | 场桥编号、所在堆场、起重量 |
| 危险品管理 | `danger` | 危险品 | 危品编号、箱号、危品类别 |
| 理货作业 | `tally` | 理货单 | 理货编号、船舶航次、理货类型 |
| 海关查验 | `customs` | 查验指令 | 指令编号、箱号、查验类型 |
| 外集卡管理 | `truck` | 外集卡 | 车辆编号、车牌号、所属车队 |
| 支线驳船 | `barge` | 驳船 | 驳船编号、驳船名称、运输航线 |
| 冷藏箱管理 | `reefer` | 冷藏箱 | 冷藏编号、箱号、设定温度 |
| 箱体修理 | `repair` | 修箱单 | 修箱编号、箱号、破损描述 |
| 铁路集疏 | `rail` | 铁路计划 | 计划编号、到站名称、车皮数量 |
| 船公司对接 | `shipping_line` | 船公司 | 公司编号、公司全称、航线代码 |
| 设备维保 | `equip_maintain` | 维保计划 | 计划编号、设备编号、设备类型 |
| 调度指令 | `dispatch` | 调度指令 | 指令编号、指令类型、执行班组 |

## 约定

- 每个模块的前端页面在 `frontend/src/views/<模块>/index.vue`，后端接口在
  `backend/app/routers/<模块>.py`，业务规则在 `backend/app/services/<模块>.py`。
- 列表接口统一返回 `{ items, total, page, size }`，动作接口统一返回 `{ ok, message }`。
- 状态流转只允许在 `app/services` 里改，路由层不做业务判断。
