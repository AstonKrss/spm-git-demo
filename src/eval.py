"""SPM内控评价模拟（EVAL模块，CB3基线）"""

def score(domain_items):
    """按内控矩阵评分：缺陷数扣分，满分100"""
    return max(0, 100 - 10 * len(domain_items))
