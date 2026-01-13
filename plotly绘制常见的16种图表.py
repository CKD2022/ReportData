import pandas as pd
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import plotly.figure_factory as ff
import numpy as np
from datetime import datetime, timedelta

# 设置页面标题和布局
st.set_page_config(page_title="Plotly图表示例大全", layout="wide")
st.title("📊 Plotly图表类型示例大全")
st.markdown("使用Plotly和Streamlit创建的各种图表类型演示")


# 生成示例数据
@st.cache_data
def generate_sample_data():
    np.random.seed(42)

    # 基础数据
    categories = ['A', 'B', 'C', 'D', 'E']
    sub_categories = ['X', 'Y', 'Z']

    # 柱状图/条形图数据
    bar_data = pd.DataFrame({
        '类别': categories * 2,
        '值': np.random.randn(10) * 100 + 50,
        '组别': ['组1'] * 5 + ['组2'] * 5
    })

    # 折线图/面积图数据
    dates = pd.date_range('2023-01-01', periods=30, freq='D')
    line_data = pd.DataFrame({
        '日期': dates,
        '系列1': np.cumsum(np.random.randn(30)) + 50,
        '系列2': np.cumsum(np.random.randn(30)) + 30,
        '系列3': np.cumsum(np.random.randn(30)) + 70
    })

    # 饼图/圆环图数据
    pie_data = pd.DataFrame({
        '项目': categories,
        '占比': np.random.rand(5) * 100
    })

    # 散点图/气泡图数据
    scatter_data = pd.DataFrame({
        'X值': np.random.randn(50) * 10,
        'Y值': np.random.randn(50) * 10,
        '大小': np.random.rand(50) * 100,
        '类别': np.random.choice(['类型1', '类型2', '类型3'], 50),
        '数值': np.random.rand(50) * 100
    })

    # 树状图/旭日图数据
    sunburst_data = pd.DataFrame({
        '国家': ['中国', '中国', '中国', '美国', '美国', '美国', '日本', '日本'],
        '产品类别': ['电子产品', '服装', '食品', '电子产品', '服装', '食品', '电子产品', '食品'],
        '子类别': ['手机', '男装', '水果', '电脑', '女装', '肉类', '相机', '海鲜'],
        '销售额': [120, 80, 60, 150, 90, 70, 100, 50]
    })

    # 直方图数据
    hist_data = np.random.randn(1000)

    # 箱线图数据
    box_data = pd.DataFrame({
        '类别': ['A'] * 100 + ['B'] * 100 + ['C'] * 100,
        '数值': np.concatenate([np.random.randn(100) + 1,
                                np.random.randn(100) + 2,
                                np.random.randn(100) + 3])
    })

    # 瀑布图数据
    waterfall_data = pd.DataFrame({
        '项目': ['收入', '成本', '运营费用', '税费', '其他', '净利润'],
        '数值': [1000, -400, -300, -100, 50, 250]
    })

    # 漏斗图数据
    funnel_data = pd.DataFrame({
        '阶段': ['访问', '注册', '试用', '购买', '复购'],
        '用户数': [1000, 800, 600, 400, 200]
    })

    # 股价图数据
    stock_dates = pd.date_range('2023-01-01', periods=20, freq='D')
    stock_data = pd.DataFrame({
        '日期': stock_dates,
        '开盘': np.cumsum(np.random.randn(20)) + 100,
        '最高': np.cumsum(np.random.randn(20)) + 105,
        '最低': np.cumsum(np.random.randn(20)) + 95,
        '收盘': np.cumsum(np.random.randn(20)) + 100,
        '交易量': np.random.randint(1000, 10000, 20)
    })

    # 地图数据
    map_data = pd.DataFrame({
        '城市': ['北京', '上海', '广州', '深圳', '杭州', '成都', '武汉', '西安'],
        '经度': [116.40, 121.47, 113.26, 114.06, 120.15, 104.07, 114.31, 108.94],
        '纬度': [39.90, 31.23, 23.12, 22.54, 30.28, 30.67, 30.52, 34.27],
        '数值': [800, 1000, 600, 700, 500, 400, 300, 350]
    })

    return {
        'bar': bar_data,
        'line': line_data,
        'pie': pie_data,
        'scatter': scatter_data,
        'sunburst': sunburst_data,
        'hist': hist_data,
        'box': box_data,
        'waterfall': waterfall_data,
        'funnel': funnel_data,
        'stock': stock_data,
        'map': map_data
    }


# 加载数据
data = generate_sample_data()

# 创建侧边栏选择图表类型
chart_type = st.sidebar.selectbox(
    "选择图表类型",
    ["柱状图", "条形图", "折线图", "面积图", "饼图", "圆环图",
     "散点图", "气泡图", "极坐标图", "树状图", "旭日图",
     "直方图", "箱线图", "瀑布图", "漏斗图", "股价图", "地图"]
)

# 根据选择的图表类型显示相应的图表
st.header(f"{chart_type}示例")

if chart_type == "柱状图":
    st.subheader("柱状图 (Bar Chart)")
    st.write("柱状图用于比较不同类别的数据")

    fig = px.bar(data['bar'], x='类别', y='值', color='组别',
                 barmode='group', title='分组柱状图示例')
    st.plotly_chart(fig, use_container_width=True)

    # 堆叠柱状图
    fig2 = px.bar(data['bar'], x='类别', y='值', color='组别',
                  barmode='stack', title='堆叠柱状图示例')
    st.plotly_chart(fig2, use_container_width=True)

elif chart_type == "条形图":
    st.subheader("条形图 (Horizontal Bar Chart)")
    st.write("条形图是横向的柱状图，适合类别名称较长的情况")

    fig = px.bar(data['bar'], y='类别', x='值', color='组别',
                 orientation='h', title='条形图示例')
    st.plotly_chart(fig, use_container_width=True)

elif chart_type == "折线图":
    st.subheader("折线图 (Line Chart)")
    st.write("折线图用于显示数据随时间变化的趋势")

    fig = px.line(data['line'], x='日期', y=['系列1', '系列2', '系列3'],
                  title='多系列折线图示例')
    st.plotly_chart(fig, use_container_width=True)

    # 带标记点的折线图
    fig2 = px.line(data['line'], x='日期', y='系列1',
                   markers=True, title='带标记点的折线图示例')
    st.plotly_chart(fig2, use_container_width=True)

elif chart_type == "面积图":
    st.subheader("面积图 (Area Chart)")
    st.write("面积图是折线图下的区域被填充的图表，用于显示累积趋势")

    fig = px.area(data['line'], x='日期', y=['系列1', '系列2', '系列3'],
                  title='堆叠面积图示例')
    st.plotly_chart(fig, use_container_width=True)

elif chart_type == "饼图":
    st.subheader("饼图 (Pie Chart)")
    st.write("饼图用于显示各部分占总体的比例")

    fig = px.pie(data['pie'], values='占比', names='项目',
                 title='饼图示例')
    st.plotly_chart(fig, use_container_width=True)

elif chart_type == "圆环图":
    st.subheader("圆环图 (Donut Chart)")
    st.write("圆环图是中间有孔的饼图，可以显示更多信息")

    fig = px.pie(data['pie'], values='占比', names='项目',
                 hole=0.4, title='圆环图示例')
    st.plotly_chart(fig, use_container_width=True)

elif chart_type == "散点图":
    st.subheader("散点图 (Scatter Plot)")
    st.write("散点图用于显示两个变量之间的关系")

    fig = px.scatter(data['scatter'], x='X值', y='Y值',
                     color='类别', title='散点图示例')
    st.plotly_chart(fig, use_container_width=True)

elif chart_type == "气泡图":
    st.subheader("气泡图 (Bubble Chart)")
    st.write("气泡图是散点图的变体，其中点的大小表示第三个变量的值")

    fig = px.scatter(data['scatter'], x='X值', y='Y值',
                     size='大小', color='类别',
                     hover_name='类别', size_max=60,
                     title='气泡图示例')
    st.plotly_chart(fig, use_container_width=True)

elif chart_type == "极坐标图":
    st.subheader("极坐标/雷达图 (Polar/Radar Chart)")
    st.write("雷达图用于显示多变量数据")

    # 创建雷达图数据
    categories = ['A', 'B', 'C', 'D', 'E']
    values1 = [4, 3, 2, 5, 1]
    values2 = [3, 1, 4, 2, 5]

    fig = go.Figure()

    fig.add_trace(go.Scatterpolar(
        r=values1,
        theta=categories,
        fill='toself',
        name='系列1'
    ))

    fig.add_trace(go.Scatterpolar(
        r=values2,
        theta=categories,
        fill='toself',
        name='系列2'
    ))

    fig.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, 6]
            )),
        showlegend=True,
        title='雷达图示例'
    )

    st.plotly_chart(fig, use_container_width=True)

elif chart_type == "树状图":
    st.subheader("树状图 (Treemap)")
    st.write("树状图用于显示分层数据，矩形大小表示数值")

    fig = px.treemap(data['sunburst'],
                     path=['国家', '产品类别', '子类别'],
                     values='销售额',
                     title='树状图示例')
    st.plotly_chart(fig, use_container_width=True)

elif chart_type == "旭日图":
    st.subheader("旭日图 (Sunburst Chart)")
    st.write("旭日图用于显示分层数据，是树状图的圆形变体")

    fig = px.sunburst(data['sunburst'],
                      path=['国家', '产品类别', '子类别'],
                      values='销售额',
                      title='旭日图示例')
    st.plotly_chart(fig, use_container_width=True)

elif chart_type == "直方图":
    st.subheader("直方图 (Histogram)")
    st.write("直方图用于显示数据分布")

    fig = px.histogram(x=data['hist'], nbins=30,
                       title='直方图示例')
    fig.update_layout(xaxis_title="值", yaxis_title="频率")
    st.plotly_chart(fig, use_container_width=True)

    # 叠加直方图
    fig2 = ff.create_distplot([np.random.randn(1000) for _ in range(3)],
                              ['系列1', '系列2', '系列3'],
                              bin_size=0.2, show_rug=False)
    fig2.update_layout(title='多系列分布图示例')
    st.plotly_chart(fig2, use_container_width=True)

elif chart_type == "箱线图":
    st.subheader("箱线图 (Box Plot)")
    st.write("箱线图用于显示数据分布和离群点")

    fig = px.box(data['box'], x='类别', y='数值',
                 title='箱线图示例')
    st.plotly_chart(fig, use_container_width=True)

    # 小提琴图
    fig2 = px.violin(data['box'], x='类别', y='数值',
                     box=True, points="all",
                     title='小提琴图示例')
    st.plotly_chart(fig2, use_container_width=True)

elif chart_type == "瀑布图":
    st.subheader("瀑布图 (Waterfall Chart)")
    st.write("瀑布图用于显示数值的累计变化")

    fig = go.Figure(go.Waterfall(
        name="财务数据",
        orientation="v",
        measure=["relative", "relative", "relative", "relative", "relative", "total"],
        x=data['waterfall']['项目'],
        textposition="outside",
        text=data['waterfall']['数值'],
        y=data['waterfall']['数值'],
        connector={"line": {"color": "rgb(63, 63, 63)"}},
    ))

    fig.update_layout(
        title="瀑布图示例 - 财务数据",
        showlegend=True
    )

    st.plotly_chart(fig, use_container_width=True)

elif chart_type == "漏斗图":
    st.subheader("漏斗图 (Funnel Chart)")
    st.write("漏斗图用于显示流程中各个阶段的转化率")

    fig = px.funnel(data['funnel'], x='用户数', y='阶段',
                    title='漏斗图示例')
    st.plotly_chart(fig, use_container_width=True)

elif chart_type == "股价图":
    st.subheader("股价图 (Candlestick Chart)")
    st.write("股价图用于显示金融市场价格变动")

    fig = go.Figure(data=[go.Candlestick(
        x=data['stock']['日期'],
        open=data['stock']['开盘'],
        high=data['stock']['最高'],
        low=data['stock']['最低'],
        close=data['stock']['收盘']
    )])

    fig.update_layout(
        title="股价图示例",
        xaxis_title="日期",
        yaxis_title="价格",
        xaxis_rangeslider_visible=False
    )

    st.plotly_chart(fig, use_container_width=True)

    # OHLC图
    st.subheader("OHLC图")
    fig2 = go.Figure(data=[go.Ohlc(
        x=data['stock']['日期'],
        open=data['stock']['开盘'],
        high=data['stock']['最高'],
        low=data['stock']['最低'],
        close=data['stock']['收盘']
    )])

    fig2.update_layout(
        title="OHLC图示例",
        xaxis_title="日期",
        yaxis_title="价格",
        xaxis_rangeslider_visible=False
    )

    st.plotly_chart(fig2, use_container_width=True)

elif chart_type == "地图":
    st.subheader("地图 (Map)")
    st.write("地图用于显示地理空间数据")

    # 散点地图
    fig = px.scatter_mapbox(data['map'],
                            lat="纬度",
                            lon="经度",
                            size="数值",
                            color="数值",
                            hover_name="城市",
                            zoom=3,
                            title="散点地图示例")

    fig.update_layout(mapbox_style="open-street-map")
    fig.update_layout(margin={"r": 0, "t": 30, "l": 0, "b": 0})
    st.plotly_chart(fig, use_container_width=True)

    # 气泡地图
    st.subheader("气泡地图")
    fig2 = px.scatter_geo(data['map'],
                          lat="纬度",
                          lon="经度",
                          size="数值",
                          color="城市",
                          hover_name="城市",
                          projection="natural earth",
                          title="气泡地图示例")

    st.plotly_chart(fig2, use_container_width=True)

# 显示数据表
with st.expander("查看当前图表使用的数据"):
    if chart_type in ["柱状图", "条形图"]:
        st.dataframe(data['bar'])
    elif chart_type in ["折线图", "面积图"]:
        st.dataframe(data['line'])
    elif chart_type in ["饼图", "圆环图"]:
        st.dataframe(data['pie'])
    elif chart_type in ["散点图", "气泡图"]:
        st.dataframe(data['scatter'])
    elif chart_type in ["树状图", "旭日图"]:
        st.dataframe(data['sunburst'])
    elif chart_type == "直方图":
        st.write("数据为1000个随机值")
    elif chart_type == "箱线图":
        st.dataframe(data['box'])
    elif chart_type == "瀑布图":
        st.dataframe(data['waterfall'])
    elif chart_type == "漏斗图":
        st.dataframe(data['funnel'])
    elif chart_type == "股价图":
        st.dataframe(data['stock'])
    elif chart_type == "地图":
        st.dataframe(data['map'])

# 添加使用说明
st.sidebar.markdown("---")
st.sidebar.info("""
### 使用说明
1. 从左侧选择图表类型
2. 图表将显示在右侧主区域
3. 可以悬停在图表上查看详细信息
4. 使用图表右上角的工具栏进行交互操作
""")