# -*- coding: utf-8 -*-
"""SPM统一门户模拟：登录与会话（PORTAL模块，CB1基线）"""

USERS = {"nkadmin": ("内控办", "admin"), "cxs": ("审计处", "audit")}

def login(user, pwd):
    """统一身份认证模拟：校验用户名口令，返回所属部门"""
    if user in USERS and USERS[user][1] == pwd:
        return {"user": user, "dept": USERS[user][0], "token": user + "-session"}
    raise ValueError("认证失败")

if __name__ == "__main__":
    print(login("nkadmin", "admin"))
