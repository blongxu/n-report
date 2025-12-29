<template>
  <div class="home">
    <section class="hero">
      <div class="hero-content">
        <img src="../assets/banner.png" style="height: 100px;" alt="">
        <h1 class="hero-title">欢迎使用白龙须N-Report</h1>
        <p class="hero-subtitle">让报表制作更高效</p>
        <button class="cta-button" onclick="window.open('https://docs.report.bailongxu.com/zh/home')">了解更多</button>
      </div>
    </section>

    <section class="features">
      <div class="container">
        <h2 class="section-title">核心特性</h2>
        <div class="features-grid">
          <div class="feature-card" v-for="feature in features" :key="feature.id">
            <div class="feature-icon">{{ feature.icon }}</div>
            <h3 class="feature-title">{{ feature.title }}</h3>
            <p class="feature-description">{{ feature.description }}</p>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script>
export default {
  name: 'Home',
  data() {
    return {
      features: [
        {
          id: 1,
          icon: '🛢️',
          title: '丰富的数据源',
          description: '支持超二十多种数据源，满足各种业务需求'
        },
        {
          id: 2,
          icon: '📦',
          title: '多种组件',
          description: '多种图标组件、快速生成各类数据看板'
        },
        {
          id: 3,
          icon: '🖊️',
          title: '划词的方式生成报表',
          description: '划词生成查询参数，支持多种方式传入列表'
        },
        {
          id: 4,
          icon: '📊',
          title: '可变报表头',
          description: '可自定义表头，适配各类复杂报表'
        }
      ]
    }
  },
}
</script>

<style scoped>
.home {
  min-height: 80vh;
}

.hero {
  background: linear-gradient(135deg, #200897 0%, #4b74a2 100%);
  color: white;
  padding: 4rem 0;
  text-align: center;
}

.hero-content {
  max-width: 800px;
  margin: 0 auto;
  padding: 0 2rem;
}

.hero-title {
  font-size: 3rem;
  margin-bottom: 1rem;
  font-weight: 700;
}

.hero-subtitle {
  font-size: 1.2rem;
  margin-bottom: 2rem;
  opacity: 0.9;
}

.cta-button {
  background: white;
  color: #667eea;
  border: none;
  padding: 1rem 2rem;
  font-size: 1.1rem;
  border-radius: 50px;
  cursor: pointer;
  transition: transform 0.3s ease;
}

.cta-button:hover {
  transform: translateY(-2px);
}

.features {
  padding: 4rem 0;
}

.container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 2rem;
}

.section-title {
  text-align: center;
  font-size: 2.5rem;
  margin-bottom: 3rem;
  color: #333;
}

.features-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 2rem;
}

.feature-card {
  background: white;
  padding: 2rem;
  border-radius: 10px;
  box-shadow: 0 5px 15px rgba(0,0,0,0.1);
  text-align: center;
  transition: transform 0.3s ease;
}

.feature-card:hover {
  transform: translateY(-5px);
}

.feature-icon {
  font-size: 3rem;
  margin-bottom: 1rem;
}

.feature-title {
  font-size: 1.2rem;
  margin-bottom: 1rem;
  color: #333;
}

.feature-description {
  color: #666;
  line-height: 1.6;
}
</style>