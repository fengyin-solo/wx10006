"""接口出入参模型：列表分页、动作结果与各模块的明细结构。"""
from __future__ import annotations

from typing import Any, Generic, TypeVar

from pydantic import BaseModel, Field

T = TypeVar("T")


class PageResult(BaseModel, Generic[T]):
    items: list[T]
    total: int
    page: int = 1
    size: int = 20


class ActionResult(BaseModel):
    ok: bool
    message: str
    entry: dict[str, Any] | None = None


class EntryPayload(BaseModel):
    """登记或修改一条业务记录时提交的字段集合。"""

    values: dict[str, Any] = Field(default_factory=dict)
    remark: str | None = None



class VesselEntry(BaseModel):
    """船舶明细结构。"""

    field_0: str | None = None  # 船舶编号
    field_1: str | None = None  # 船名
    field_2: str | None = None  # 航次号
    field_3: str | None = None  # 预计到港
    field_4: str | None = None  # 实际到港
    field_5: str | None = None  # 泊位编号
    field_6: str | None = None  # 引航员
    field_7: str | None = None  # 船舶状态

class BerthEntry(BaseModel):
    """码头泊位明细结构。"""

    field_0: str | None = None  # 泊位编号
    field_1: str | None = None  # 泊位名称
    field_2: str | None = None  # 靠泊能力
    field_3: str | None = None  # 前沿水深
    field_4: str | None = None  # 岸桥配置
    field_5: str | None = None  # 占用时间起
    field_6: str | None = None  # 占用时间止
    field_7: str | None = None  # 泊位状态

class CraneEntry(BaseModel):
    """岸桥明细结构。"""

    field_0: str | None = None  # 岸桥编号
    field_1: str | None = None  # 所在泊位
    field_2: str | None = None  # 吊具类型
    field_3: str | None = None  # 额定起重量
    field_4: str | None = None  # 作业效率
    field_5: str | None = None  # 当前箱量
    field_6: str | None = None  # 操作司机
    field_7: str | None = None  # 岸桥状态

class YardEntry(BaseModel):
    """堆场贝位明细结构。"""

    field_0: str | None = None  # 贝位编号
    field_1: str | None = None  # 所属堆场
    field_2: str | None = None  # 箱区类型
    field_3: str | None = None  # 排位号
    field_4: str | None = None  # 层高
    field_5: str | None = None  # 当前堆存
    field_6: str | None = None  # 最大容量
    field_7: str | None = None  # 贝位状态

class ContainerEntry(BaseModel):
    """集装箱明细结构。"""

    field_0: str | None = None  # 箱号
    field_1: str | None = None  # 箱型尺寸
    field_2: str | None = None  # 箱公司
    field_3: str | None = None  # 提单号
    field_4: str | None = None  # 卸货港
    field_5: str | None = None  # 进场时间
    field_6: str | None = None  # 堆存位置
    field_7: str | None = None  # 箱体状态

class GateEntry(BaseModel):
    """进出记录明细结构。"""

    field_0: str | None = None  # 记录编号
    field_1: str | None = None  # 箱号
    field_2: str | None = None  # 车牌号
    field_3: str | None = None  # 进出方向
    field_4: str | None = None  # 是否重箱
    field_5: str | None = None  # 过闸时间
    field_6: str | None = None  # 放行岗亭
    field_7: str | None = None  # 记录状态

class YcEntry(BaseModel):
    """场桥明细结构。"""

    field_0: str | None = None  # 场桥编号
    field_1: str | None = None  # 所在堆场
    field_2: str | None = None  # 起重量
    field_3: str | None = None  # 跨距
    field_4: str | None = None  # 作业箱量
    field_5: str | None = None  # 操作司机
    field_6: str | None = None  # 油耗量
    field_7: str | None = None  # 场桥状态

class DangerEntry(BaseModel):
    """危险品明细结构。"""

    field_0: str | None = None  # 危品编号
    field_1: str | None = None  # 箱号
    field_2: str | None = None  # 危品类别
    field_3: str | None = None  # UN编号
    field_4: str | None = None  # 堆存位置
    field_5: str | None = None  # 隔离要求
    field_6: str | None = None  # 入库日期
    field_7: str | None = None  # 危品状态

class TallyEntry(BaseModel):
    """理货单明细结构。"""

    field_0: str | None = None  # 理货编号
    field_1: str | None = None  # 船舶航次
    field_2: str | None = None  # 理货类型
    field_3: str | None = None  # 计划箱数
    field_4: str | None = None  # 实际箱数
    field_5: str | None = None  # 残损箱数
    field_6: str | None = None  # 理货长
    field_7: str | None = None  # 理货状态

class CustomsEntry(BaseModel):
    """查验指令明细结构。"""

    field_0: str | None = None  # 指令编号
    field_1: str | None = None  # 箱号
    field_2: str | None = None  # 查验类型
    field_3: str | None = None  # 布控原因
    field_4: str | None = None  # 通知时间
    field_5: str | None = None  # 查验结果
    field_6: str | None = None  # 放行时间
    field_7: str | None = None  # 指令状态

class TruckEntry(BaseModel):
    """外集卡明细结构。"""

    field_0: str | None = None  # 车辆编号
    field_1: str | None = None  # 车牌号
    field_2: str | None = None  # 所属车队
    field_3: str | None = None  # 进港时间
    field_4: str | None = None  # 提箱单号
    field_5: str | None = None  # 绑定司机
    field_6: str | None = None  # 作业状态
    field_7: str | None = None  # 出场时间

class BargeEntry(BaseModel):
    """驳船明细结构。"""

    field_0: str | None = None  # 驳船编号
    field_1: str | None = None  # 驳船名称
    field_2: str | None = None  # 运输航线
    field_3: str | None = None  # 计划箱量
    field_4: str | None = None  # 实际箱量
    field_5: str | None = None  # 到港时间
    field_6: str | None = None  # 离港时间
    field_7: str | None = None  # 驳船状态

class ReeferEntry(BaseModel):
    """冷藏箱明细结构。"""

    field_0: str | None = None  # 冷藏编号
    field_1: str | None = None  # 箱号
    field_2: str | None = None  # 设定温度
    field_3: str | None = None  # 当前温度
    field_4: str | None = None  # 插电位置
    field_5: str | None = None  # 接入时间
    field_6: str | None = None  # 报警状态
    field_7: str | None = None  # 监控状态

class RepairEntry(BaseModel):
    """修箱单明细结构。"""

    field_0: str | None = None  # 修箱编号
    field_1: str | None = None  # 箱号
    field_2: str | None = None  # 破损描述
    field_3: str | None = None  # 修理部位
    field_4: str | None = None  # 修理班组
    field_5: str | None = None  # 开工时间
    field_6: str | None = None  # 完工时间
    field_7: str | None = None  # 修箱状态

class RailEntry(BaseModel):
    """铁路计划明细结构。"""

    field_0: str | None = None  # 计划编号
    field_1: str | None = None  # 到站名称
    field_2: str | None = None  # 车皮数量
    field_3: str | None = None  # 计划箱量
    field_4: str | None = None  # 到站日期
    field_5: str | None = None  # 装车股道
    field_6: str | None = None  # 发车时间
    field_7: str | None = None  # 计划状态

class ShippingLineEntry(BaseModel):
    """船公司明细结构。"""

    field_0: str | None = None  # 公司编号
    field_1: str | None = None  # 公司全称
    field_2: str | None = None  # 航线代码
    field_3: str | None = None  # 协议类型
    field_4: str | None = None  # 箱量配额
    field_5: str | None = None  # 联系人
    field_6: str | None = None  # 联系电话
    field_7: str | None = None  # 合作状态

class EquipMaintainEntry(BaseModel):
    """维保计划明细结构。"""

    field_0: str | None = None  # 计划编号
    field_1: str | None = None  # 设备编号
    field_2: str | None = None  # 设备类型
    field_3: str | None = None  # 维保级别
    field_4: str | None = None  # 计划日期
    field_5: str | None = None  # 维保班组
    field_6: str | None = None  # 验收人员
    field_7: str | None = None  # 计划状态

class DispatchEntry(BaseModel):
    """调度指令明细结构。"""

    field_0: str | None = None  # 指令编号
    field_1: str | None = None  # 指令类型
    field_2: str | None = None  # 执行班组
    field_3: str | None = None  # 下发时间
    field_4: str | None = None  # 截止时间
    field_5: str | None = None  # 完成时间
    field_6: str | None = None  # 指令内容
    field_7: str | None = None  # 指令状态
