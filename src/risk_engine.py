# -*- coding: utf-8 -*-
"""SPM风险规则引擎模拟（RISK模块，CB2基线）"""

THRESHOLD = 1.10  # 预算执行率预警阈值

def evaluate(item):
    """按内控规则评估单条业务数据，返回预警列表"""
    alerts = []
    rate = item.get("budget_used_rate", 0)
    if rate > THRESHOLD:
        alerts.append({"rule": "R001", "level": "高",
                       "msg": "预算执行率%.0f%%超过110%%" % (rate * 100)})
    if item.get("paid") and not item.get("contract_no"):
        alerts.append({"rule": "R002", "level": "高",
                       "msg": "未登记合同先行付款"})
    return alerts

if __name__ == "__main__":
    demo = {"budget_used_rate": 1.25, "paid": True, "contract_no": None}
    for a in evaluate(demo):
        print(a)
