"""业务模块路由汇总。

这里统一按别名导入再暴露 ROUTERS：模块名有可能和内置名撞车（某个业务模块就叫 dict、list
这种名字时），按名字直接 import 会把内置类型覆盖掉，函数注解在运行时求值就会报
'module' object is not subscriptable。
"""
from __future__ import annotations

from app.routers import vessel as router_vessel
from app.routers import berth as router_berth
from app.routers import crane as router_crane
from app.routers import yard as router_yard
from app.routers import container as router_container
from app.routers import gate as router_gate
from app.routers import yc as router_yc
from app.routers import danger as router_danger
from app.routers import tally as router_tally
from app.routers import customs as router_customs
from app.routers import truck as router_truck
from app.routers import barge as router_barge
from app.routers import reefer as router_reefer
from app.routers import repair as router_repair
from app.routers import rail as router_rail
from app.routers import shipping_line as router_shipping_line
from app.routers import equip_maintain as router_equip_maintain
from app.routers import dispatch as router_dispatch

ROUTERS = [router_vessel, router_berth, router_crane, router_yard, router_container, router_gate, router_yc, router_danger, router_tally, router_customs, router_truck, router_barge, router_reefer, router_repair, router_rail, router_shipping_line, router_equip_maintain, router_dispatch]
