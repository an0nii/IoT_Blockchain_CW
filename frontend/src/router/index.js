import { createRouter, createWebHistory } from 'vue-router'
import HomePage from '../views/HomePage.vue'
import AddDevice from '../views/AddDevice.vue'
import DeviceDetails from '../views/DeviceDetails.vue'
import ProductList from '../views/ProductList.vue'
import ProductDetails from '../views/ProductDetails.vue'

const routes = [
  {
    path: '/',
    name: 'HomePage',
    component: HomePage
  },
  {
    path: '/add-device',
    name: 'AddDevice',
    component: AddDevice
  },
  {
    path: '/device/:id',
    name: 'DeviceDetails',
    component: DeviceDetails,
    props: true
  },
  {
    path: '/products',
    name: 'ProductList',
    component: ProductList
  },
  {
    path: '/product/:id',
    name: 'ProductDetails',
    component: ProductDetails,
    props: true
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router