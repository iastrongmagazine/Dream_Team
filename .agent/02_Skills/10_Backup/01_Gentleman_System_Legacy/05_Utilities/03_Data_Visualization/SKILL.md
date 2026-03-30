# 25 Data Visualization

## Trigger
Cuando el usuario menciona: "chart", "dashboard", "visualization", "graphs", "metrics", "analytics", "gráfico", "tabla de datos", "kpi", "Reporting"

## Overview
Skill para crear visualizaciones de datos SOTA usando las mejores librerías 2025-2026. Enfocado en TypeScript strict mode, shadcn/ui patterns, y dashboards responsivos.

---

## SOTA Stack (2025-2026)

### Libraries Ranking

| Library | Best For | Weekly DLs | Bundle | Type |
|---------|----------|------------|--------|------|
| **Recharts v2** | React apps, composable | ~3M | ~45kB gz | SVG |
| **Chart.js v4** | Simple, Canvas | ~10M | ~75kB gz | Canvas |
| **ECharts v5** | Enterprise dashboards | ~2M | ~350kB gz | Canvas |
| **Tremor v3** | SaaS dashboards | ~100k | ~200kB | React+Tailwind |
| **Nivo v0.87** | Complex viz, SSR | ~450k | Modular | SVG+Canvas |
| **D3.js v7** | Custom, max control | ~9M | ~90kB | Low-level |
| **Observable Plot** | Exploratory analysis | - | D3-powered | SVG |
| **ApexCharts** | React/Vue wrappers | ~500k | ~130kB | SVG |

### Selection Matrix

| Criteria | Winner | Alternative |
|----------|--------|------------|
| React + TypeScript strict | Recharts | Tremor |
| SaaS Dashboard (Tailwind) | Tremor | Recharts + shadcn |
| Enterprise (complex charts) | ECharts | Highcharts |
| SSR/Next.js | Nivo | Recharts |
| Max customization | D3.js | Observable Plot |
| Quick/simple charts | Chart.js | Recharts |

---

## Implementation Patterns

### 1. Recharts + shadcn/ui (RECOMMENDED)

#### Setup
```bash
npm install recharts
```

#### Bar Chart
```typescript
// components/charts/sales-chart.tsx
'use client';

import {
  BarChart,
  Bar,
  XAxis,
  YAxis,
  CartesianGrid,
  Tooltip,
  ResponsiveContainer,
  Legend,
} from 'recharts';
import {
  Card,
  CardContent,
  CardDescription,
  CardHeader,
  CardTitle,
} from '@/components/ui/card';

interface SalesData {
  month: string;
  revenue: number;
  expenses: number;
}

const data: SalesData[] = [
  { month: 'Ene', revenue: 4000, expenses: 2400 },
  { month: 'Feb', revenue: 3000, expenses: 1398 },
  { month: 'Mar', revenue: 2000, expenses: 9800 },
  { month: 'Abr', revenue: 2780, expenses: 3908 },
  { month: 'May', revenue: 1890, expenses: 4800 },
  { month: 'Jun', revenue: 2390, expenses: 3800 },
];

interface SalesChartProps {
  data?: SalesData[];
  className?: string;
}

export function SalesChart({ data: chartData = data, className }: SalesChartProps) {
  return (
    <Card className={className}>
      <CardHeader>
        <CardTitle>Revenue vs Expenses</CardTitle>
        <CardDescription>Monthly comparison 2026</CardDescription>
      </CardHeader>
      <CardContent>
        <ResponsiveContainer width="100%" height={300}>
          <BarChart data={chartData}>
            <CartesianGrid strokeDasharray="3 3" className="stroke-muted" />
            <XAxis
              dataKey="month"
              className="text-xs"
              tick={{ fill: 'hsl(var(--muted-foreground))' }}
            />
            <YAxis
              className="text-xs"
              tick={{ fill: 'hsl(var(--muted-foreground))' }}
              tickFormatter={(value) => `$${value / 1000}k`}
            />
            <Tooltip
              contentStyle={{
                backgroundColor: 'hsl(var(--card))',
                border: '1px solid hsl(var(--border))',
                borderRadius: 'var(--radius)',
              }}
              formatter={(value: number) => [`$${value.toLocaleString()}`, '']}
            />
            <Legend />
            <Bar dataKey="revenue" name="Revenue" fill="hsl(var(--primary))" radius={[4, 4, 0, 0]} />
            <Bar dataKey="expenses" name="Expenses" fill="hsl(var(--destructive))" radius={[4, 4, 0, 0]} />
          </BarChart>
        </ResponsiveContainer>
      </CardContent>
    </Card>
  );
}
```

#### Line Chart with Real-time Updates
```typescript
// components/charts/metrics-line-chart.tsx
'use client';

import { useEffect, useState, useCallback, useRef } from 'react';
import {
  LineChart,
  Line,
  XAxis,
  YAxis,
  CartesianGrid,
  Tooltip,
  ResponsiveContainer,
  Area,
  ComposedChart,
} from 'recharts';
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card';

interface MetricPoint {
  timestamp: number;
  value: number;
  label: string;
}

interface MetricsLineChartProps {
  title?: string;
  metricKey?: string;
  color?: string;
  maxPoints?: number;
  websocketUrl?: string;
}

export function MetricsLineChart({
  title = 'System Metrics',
  metricKey = 'cpu',
  color = 'hsl(var(--primary))',
  maxPoints = 60,
}: MetricsLineChartProps) {
  const [data, setData] = useState<MetricPoint[]>([]);
  const wsRef = useRef<WebSocket | null>(null);

  const addDataPoint = useCallback((value: number) => {
    const now = Date.now();
    setData((prev) => {
      const newData = [
        ...prev,
        {
          timestamp: now,
          value,
          label: new Date(now).toLocaleTimeString(),
        },
      ].slice(-maxPoints);
      return newData;
    });
  }, [maxPoints]);

  useEffect(() => {
    const interval = setInterval(() => {
      const value = Math.random() * 100;
      addDataPoint(value);
    }, 1000);

    return () => clearInterval(interval);
  }, [addDataPoint]);

  return (
    <Card>
      <CardHeader>
        <CardTitle>{title}</CardTitle>
      </CardHeader>
      <CardContent>
        <ResponsiveContainer width="100%" height={250}>
          <ComposedChart data={data}>
            <defs>
              <linearGradient id={`gradient-${metricKey}`} x1="0" y1="0" x2="0" y2="1">
                <stop offset="5%" stopColor={color} stopOpacity={0.3} />
                <stop offset="95%" stopColor={color} stopOpacity={0} />
              </linearGradient>
            </defs>
            <CartesianGrid strokeDasharray="3 3" className="stroke-muted" />
            <XAxis
              dataKey="label"
              className="text-xs"
              tick={{ fill: 'hsl(var(--muted-foreground))', fontSize: 10 }}
              interval="preserveStartEnd"
            />
            <YAxis
              domain={[0, 100]}
              className="text-xs"
              tick={{ fill: 'hsl(var(--muted-foreground))' }}
              tickFormatter={(v) => `${v}%`}
            />
            <Tooltip
              contentStyle={{
                backgroundColor: 'hsl(var(--card))',
                border: '1px solid hsl(var(--border))',
                borderRadius: 'var(--radius)',
              }}
              formatter={(value: number) => [`${value.toFixed(1)}%`, 'Usage']}
            />
            <Area
              type="monotone"
              dataKey="value"
              stroke="transparent"
              fill={`url(#gradient-${metricKey})`}
            />
            <Line
              type="monotone"
              dataKey="value"
              stroke={color}
              strokeWidth={2}
              dot={false}
              isAnimationActive={false}
            />
          </ComposedChart>
        </ResponsiveContainer>
      </CardContent>
    </Card>
  );
}
```

#### Pie/Donut Chart
```typescript
// components/charts/distribution-chart.tsx
'use client';

import { PieChart, Pie, Cell, ResponsiveContainer, Tooltip, Legend } from 'recharts';
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card';

interface DistributionData {
  name: string;
  value: number;
  color: string;
}

interface DistributionChartProps {
  title?: string;
  data: DistributionData[];
  showLegend?: boolean;
  innerRadius?: number;
  outerRadius?: number;
}

export function DistributionChart({
  title = 'Distribution',
  data,
  showLegend = true,
  innerRadius = 60,
  outerRadius = 100,
}: DistributionChartProps) {
  const total = data.reduce((sum, item) => sum + item.value, 0);

  return (
    <Card>
      <CardHeader>
        <CardTitle>{title}</CardTitle>
      </CardHeader>
      <CardContent>
        <ResponsiveContainer width="100%" height={300}>
          <PieChart>
            <Pie
              data={data}
              cx="50%"
              cy="50%"
              innerRadius={innerRadius}
              outerRadius={outerRadius}
              paddingAngle={2}
              dataKey="value"
              nameKey="name"
            >
              {data.map((entry, index) => (
                <Cell key={`cell-${index}`} fill={entry.color} />
              ))}
            </Pie>
            <Tooltip
              contentStyle={{
                backgroundColor: 'hsl(var(--card))',
                border: '1px solid hsl(var(--border))',
                borderRadius: 'var(--radius)',
              }}
              formatter={(value: number, name: string) => [
                `${((value / total) * 100).toFixed(1)}%`,
                name,
              ]}
            />
            {showLegend && (
              <Legend
                formatter={(value) => (
                  <span className="text-xs text-muted-foreground">{value}</span>
                )}
              />
            )}
          </PieChart>
        </ResponsiveContainer>
        <div className="mt-4 text-center">
          <p className="text-2xl font-bold">{total.toLocaleString()}</p>
          <p className="text-xs text-muted-foreground">Total</p>
        </div>
      </CardContent>
    </Card>
  );
}
```

#### Area Chart
```typescript
// components/charts/area-comparison-chart.tsx
'use client';

import {
  AreaChart,
  Area,
  XAxis,
  YAxis,
  CartesianGrid,
  Tooltip,
  ResponsiveContainer,
  Legend,
} from 'recharts';
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card';

interface TrendData {
  date: string;
  productA: number;
  productB: number;
  productC: number;
}

const trendData: TrendData[] = [
  { date: 'Q1 2025', productA: 1200, productB: 800, productC: 400 },
  { date: 'Q2 2025', productA: 1400, productB: 1000, productC: 600 },
  { date: 'Q3 2025', productA: 1300, productB: 1100, productC: 800 },
  { date: 'Q4 2025', productA: 1600, productB: 1300, productC: 1000 },
  { date: 'Q1 2026', productA: 1800, productB: 1500, productC: 1200 },
];

const COLORS = ['hsl(var(--primary))', 'hsl(var(--secondary))', 'hsl(var(--accent))'];

export function AreaComparisonChart({ className }: { className?: string }) {
  return (
    <Card className={className}>
      <CardHeader>
        <CardTitle>Product Performance Trends</CardTitle>
      </CardHeader>
      <CardContent>
        <ResponsiveContainer width="100%" height={350}>
          <AreaChart data={trendData}>
            <CartesianGrid strokeDasharray="3 3" className="stroke-muted" />
            <XAxis dataKey="date" className="text-xs" />
            <YAxis className="text-xs" tickFormatter={(v) => `${v / 1000}k`} />
            <Tooltip
              contentStyle={{
                backgroundColor: 'hsl(var(--card))',
                border: '1px solid hsl(var(--border))',
                borderRadius: 'var(--radius)',
              }}
            />
            <Legend />
            {['productA', 'productB', 'productC'].map((key, index) => (
              <Area
                key={key}
                type="monotone"
                dataKey={key}
                stackId="1"
                stroke={COLORS[index]}
                fill={COLORS[index]}
                fillOpacity={0.6}
              />
            ))}
          </AreaChart>
        </ResponsiveContainer>
      </CardContent>
    </Card>
  );
}
```

#### Composed Chart (Bar + Line)
```typescript
// components/charts/kpi-composed-chart.tsx
'use client';

import {
  ComposedChart,
  Bar,
  Line,
  XAxis,
  YAxis,
  CartesianGrid,
  Tooltip,
  Legend,
  ResponsiveContainer,
} from 'recharts';
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card';

interface KPIData {
  month: string;
  sales: number;
  target: number;
  conversion: number;
}

const kpiData: KPIData[] = [
  { month: 'Ene', sales: 40000, target: 35000, conversion: 3.2 },
  { month: 'Feb', sales: 38000, target: 40000, conversion: 2.8 },
  { month: 'Mar', sales: 52000, target: 45000, conversion: 4.1 },
  { month: 'Abr', sales: 48000, target: 50000, conversion: 3.6 },
  { month: 'May', sales: 61000, target: 55000, conversion: 4.8 },
  { month: 'Jun', sales: 58000, target: 60000, conversion: 4.2 },
];

export function KPIComposedChart({ className }: { className?: string }) {
  return (
    <Card className={className}>
      <CardHeader>
        <CardTitle>Sales Performance vs Target</CardTitle>
      </CardHeader>
      <CardContent>
        <ResponsiveContainer width="100%" height={350}>
          <ComposedChart data={kpiData}>
            <CartesianGrid strokeDasharray="3 3" className="stroke-muted" />
            <XAxis dataKey="month" className="text-xs" />
            <YAxis
              yAxisId="left"
              className="text-xs"
              tickFormatter={(v) => `$${v / 1000}k`}
            />
            <YAxis
              yAxisId="right"
              orientation="right"
              className="text-xs"
              tickFormatter={(v) => `${v}%`}
            />
            <Tooltip
              contentStyle={{
                backgroundColor: 'hsl(var(--card))',
                border: '1px solid hsl(var(--border))',
                borderRadius: 'var(--radius)',
              }}
              formatter={(value: number, name: string) => {
                if (name === 'conversion') return [`${value}%`, 'Conversion'];
                return [`$${value.toLocaleString()}`, name];
              }}
            />
            <Legend />
            <Bar yAxisId="left" dataKey="sales" name="Sales" fill="hsl(var(--primary))" radius={[4, 4, 0, 0]} />
            <Bar yAxisId="left" dataKey="target" name="Target" fill="hsl(var(--muted))" radius={[4, 4, 0, 0]} />
            <Line
              yAxisId="right"
              type="monotone"
              dataKey="conversion"
              name="Conversion %"
              stroke="hsl(var(--accent))"
              strokeWidth={2}
              dot={{ fill: 'hsl(var(--accent))', r: 4 }}
            />
          </ComposedChart>
        </ResponsiveContainer>
      </CardContent>
    </Card>
  );
}
```

---

### 2. Tremor for SaaS Dashboard

#### Setup
```bash
npm install @tremor/react
```

#### KPI Card
```typescript
// components/dashboard/kpi-card.tsx
'use client';

import { Card, Metric, Text, Flex, ProgressBar, Badge } from '@tremor/react';

interface KPICardProps {
  title: string;
  metric: string | number;
  metricFormat?: 'number' | 'currency' | 'percent';
  change?: number;
  changeType?: 'positive' | 'negative' | 'neutral';
  progress?: number;
  target?: string;
}

export function KPICard({
  title,
  metric,
  metricFormat = 'number',
  change,
  changeType = 'positive',
  progress,
  target,
}: KPICardProps) {
  const formatMetric = (value: string | number) => {
    if (typeof value === 'number') {
      switch (metricFormat) {
        case 'currency':
          return new Intl.NumberFormat('en-US', {
            style: 'currency',
            currency: 'USD',
            maximumFractionDigits: 0,
          }).format(value);
        case 'percent':
          return `${value.toFixed(1)}%`;
        default:
          return value.toLocaleString();
      }
    }
    return value;
  };

  return (
    <Card className="w-full">
      <Flex alignItems="start">
        <div>
          <Text>{title}</Text>
          <Metric>{formatMetric(metric)}</Metric>
        </div>
        {change !== undefined && (
          <Badge color={changeType === 'positive' ? 'emerald' : changeType === 'negative' ? 'rose' : 'gray'}>
            {change > 0 ? '+' : ''}{change}%
          </Badge>
        )}
      </Flex>
      {progress !== undefined && (
        <Flex className="mt-4">
          <Text>{progress}% of {target}</Text>
        </Flex>
      )}
      {progress !== undefined && (
        <ProgressBar value={progress} color="emerald" className="mt-2" />
      )}
    </Card>
  );
}
```

#### Dashboard Layout
```typescript
// components/dashboard/sales-dashboard.tsx
'use client';

import { Card, Title, AreaChart, BarChart, TabGroup, TabList, Tab, Table, TableHead, TableRow, TableHeaderCell, TableBody, TableCell, Badge } from '@tremor/react';

const salesData = [
  { month: 'Ene', Sales: 45000, Leads: 1200 },
  { month: 'Feb', Sales: 52000, Leads: 1400 },
  { month: 'Mar', Sales: 48000, Leads: 1350 },
  { month: 'Abr', Sales: 61000, Leads: 1600 },
];

const categories = ['Q1', 'Q2', 'Q3', 'Q4'];

const categoryData = categories.map((cat) => ({
  name: cat,
  Sales: Math.floor(Math.random() * 50000) + 30000,
  Customers: Math.floor(Math.random() * 500) + 200,
}));

const transactions = [
  { id: 1, customer: 'Acme Corp', amount: 12500, status: 'completed', date: '2026-03-15' },
  { id: 2, customer: 'TechStart', amount: 8200, status: 'pending', date: '2026-03-14' },
  { id: 3, customer: 'GlobalSys', amount: 15800, status: 'completed', date: '2026-03-14' },
  { id: 4, customer: 'DataFlow', amount: 6400, status: 'failed', date: '2026-03-13' },
];

export function SalesDashboard() {
  return (
    <div className="p-8 space-y-6">
      <Title>Sales Dashboard</Title>

      <TabGroup>
        <TabList>
          <Tab>Overview</Tab>
          <Tab>Analytics</Tab>
          <Tab>Reports</Tab>
        </TabList>
      </TabGroup>

      <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
        <Card>
          <Title>Revenue Trend</Title>
          <AreaChart
            className="h-64 mt-4"
            data={salesData}
            index="month"
            categories={['Sales']}
            colors={['emerald']}
            valueFormatter={(v) => `$${v.toLocaleString()}`}
          />
        </Card>

        <Card>
          <Title>Performance by Category</Title>
          <BarChart
            className="h-64 mt-4"
            data={categoryData}
            index="name"
            categories={['Sales', 'Customers']}
            colors={['emerald', 'blue']}
            valueFormatter={(v) => v.toLocaleString()}
          />
        </Card>
      </div>

      <Card>
        <Title>Recent Transactions</Title>
        <Table className="mt-4">
          <TableHead>
            <TableRow>
              <TableHeaderCell>Customer</TableHeaderCell>
              <TableHeaderCell>Amount</TableHeaderCell>
              <TableHeaderCell>Status</TableHeaderCell>
              <TableHeaderCell>Date</TableHeaderCell>
            </TableRow>
          </TableHead>
          <TableBody>
            {transactions.map((tx) => (
              <TableRow key={tx.id}>
                <TableCell>{tx.customer}</TableCell>
                <TableCell>${tx.amount.toLocaleString()}</TableCell>
                <TableCell>
                  <Badge
                    color={
                      tx.status === 'completed' ? 'emerald' :
                      tx.status === 'pending' ? 'amber' : 'rose'
                    }
                  >
                    {tx.status}
                  </Badge>
                </TableCell>
                <TableCell>{tx.date}</TableCell>
              </TableRow>
            ))}
          </TableBody>
        </Table>
      </Card>
    </div>
  );
}
```

---

### 3. TanStack Table + Charts Integration

```typescript
// components/dashboard/table-chart-integration.tsx
'use client';

import { useMemo } from 'react';
import {
  ColumnDef,
  flexRender,
  getCoreRowModel,
  useReactTable,
  getSortedRowModel,
  SortingState,
} from '@tanstack/react-table';
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card';
import {
  Table,
  TableBody,
  TableCell,
  TableHead,
  TableHeader,
  TableRow,
} from '@/components/ui/table';
import { ArrowUpDown, ArrowUp, ArrowDown } from 'lucide-react';
import { Button } from '@/components/ui/button';
import { BarChart, Bar, XAxis, YAxis, Tooltip, ResponsiveContainer } from 'recharts';

interface SalesRecord {
  id: string;
  product: string;
  revenue: number;
  units: number;
  growth: number;
  region: string;
}

const salesData: SalesRecord[] = [
  { id: '1', product: 'Enterprise Suite', revenue: 245000, units: 45, growth: 12.5, region: 'North America' },
  { id: '2', product: 'Pro License', revenue: 189000, units: 312, growth: 8.2, region: 'Europe' },
  { id: '3', product: 'Starter Plan', revenue: 78000, units: 890, growth: -2.1, region: 'Asia Pacific' },
  { id: '4', product: 'Add-ons', revenue: 56000, units: 1240, growth: 15.7, region: 'North America' },
  { id: '5', product: 'Support Package', revenue: 42000, units: 380, growth: 5.3, region: 'Europe' },
];

export function TableChartDashboard() {
  const [sorting, setSorting] = React.useState<SortingState>([]);

  const columns = useMemo<ColumnDef<SalesRecord>[]>(
    () => [
      {
        accessorKey: 'product',
        header: ({ column }) => (
          <Button
            variant="ghost"
            onClick={() => column.toggleSorting(column.getIsSorted() === 'asc')}
          >
            Product
            {column.getIsSorted() === 'asc' ? (
              <ArrowUp className="ml-2 h-4 w-4" />
            ) : column.getIsSorted() === 'desc' ? (
              <ArrowDown className="ml-2 h-4 w-4" />
            ) : (
              <ArrowUpDown className="ml-2 h-4 w-4" />
            )}
          </Button>
        ),
      },
      {
        accessorKey: 'revenue',
        header: ({ column }) => (
          <Button
            variant="ghost"
            onClick={() => column.toggleSorting(column.getIsSorted() === 'asc')}
          >
            Revenue
            {column.getIsSorted() === 'asc' ? (
              <ArrowUp className="ml-2 h-4 w-4" />
            ) : column.getIsSorted() === 'desc' ? (
              <ArrowDown className="ml-2 h-4 w-4" />
            ) : (
              <ArrowUpDown className="ml-2 h-4 w-4" />
            )}
          </Button>
        ),
        cell: ({ row }) => `$${row.original.revenue.toLocaleString()}`,
      },
      {
        accessorKey: 'units',
        header: ({ column }) => (
          <Button
            variant="ghost"
            onClick={() => column.toggleSorting(column.getIsSorted() === 'asc')}
          >
            Units
            {column.getIsSorted() === 'asc' ? (
              <ArrowUp className="ml-2 h-4 w-4" />
            ) : column.getIsSorted() === 'desc' ? (
              <ArrowDown className="ml-2 h-4 w-4" />
            ) : (
              <ArrowUpDown className="ml-2 h-4 w-4" />
            )}
          </Button>
        ),
      },
      {
        accessorKey: 'growth',
        header: 'Growth',
        cell: ({ row }) => (
          <span className={row.original.growth >= 0 ? 'text-green-600' : 'text-red-600'}>
            {row.original.growth >= 0 ? '+' : ''}{row.original.growth}%
          </span>
        ),
      },
      {
        accessorKey: 'region',
        header: 'Region',
      },
    ],
    []
  );

  const table = useReactTable({
    data: salesData,
    columns,
    state: { sorting },
    onSortingChange: setSorting,
    getCoreRowModel: getCoreRowModel(),
    getSortedRowModel: getSortedRowModel(),
  });

  const chartData = useMemo(
    () =>
      table
        .getRowModel()
        .rows.map((row) => ({
          name: row.original.product,
          revenue: row.original.revenue,
        }))
        .reverse()
        .slice(0, 5),
    [table.getRowModel().rows]
  );

  const totalRevenue = salesData.reduce((sum, d) => sum + d.revenue, 0);
  const totalUnits = salesData.reduce((sum, d) => sum + d.units, 0);
  const avgGrowth = salesData.reduce((sum, d) => sum + d.growth, 0) / salesData.length;

  return (
    <div className="space-y-6">
      <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
        <Card>
          <CardHeader className="pb-2">
            <CardTitle className="text-sm font-medium text-muted-foreground">
              Total Revenue
            </CardTitle>
          </CardHeader>
          <CardContent>
            <div className="text-2xl font-bold">${(totalRevenue / 1000).toFixed(0)}K</div>
          </CardContent>
        </Card>
        <Card>
          <CardHeader className="pb-2">
            <CardTitle className="text-sm font-medium text-muted-foreground">
              Total Units
            </CardTitle>
          </CardHeader>
          <CardContent>
            <div className="text-2xl font-bold">{totalUnits.toLocaleString()}</div>
          </CardContent>
        </Card>
        <Card>
          <CardHeader className="pb-2">
            <CardTitle className="text-sm font-medium text-muted-foreground">
              Avg Growth
            </CardTitle>
          </CardHeader>
          <CardContent>
            <div className={`text-2xl font-bold ${avgGrowth >= 0 ? 'text-green-600' : 'text-red-600'}`}>
              {avgGrowth >= 0 ? '+' : ''}{avgGrowth.toFixed(1)}%
            </div>
          </CardContent>
        </Card>
      </div>

      <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
        <Card>
          <CardHeader>
            <CardTitle>Top Products by Revenue</CardTitle>
          </CardHeader>
          <CardContent>
            <ResponsiveContainer width="100%" height={300}>
              <BarChart data={chartData} layout="vertical">
                <XAxis type="number" tickFormatter={(v) => `$${v / 1000}k`} />
                <YAxis type="category" dataKey="name" width={100} tick={{ fontSize: 12 }} />
                <Tooltip formatter={(value: number) => [`$${value.toLocaleString()}`, 'Revenue']} />
                <Bar dataKey="revenue" fill="hsl(var(--primary))" radius={[0, 4, 4, 0]} />
              </BarChart>
            </ResponsiveContainer>
          </CardContent>
        </Card>

        <Card>
          <CardHeader>
            <CardTitle>Sales Data</CardTitle>
          </CardHeader>
          <CardContent>
            <div className="rounded-md border">
              <Table>
                <TableHeader>
                  {table.getHeaderGroups().map((headerGroup) => (
                    <TableRow key={headerGroup.id}>
                      {headerGroup.headers.map((header) => (
                        <TableHead key={header.id}>
                          {header.isPlaceholder
                            ? null
                            : flexRender(header.column.columnDef.header, header.getContext())}
                        </TableHead>
                      ))}
                    </TableRow>
                  ))}
                </TableHeader>
                <TableBody>
                  {table.getRowModel().rows?.length ? (
                    table.getRowModel().rows.map((row) => (
                      <TableRow key={row.id}>
                        {row.getVisibleCells().map((cell) => (
                          <TableCell key={cell.id}>
                            {flexRender(cell.column.columnDef.cell, cell.getContext())}
                          </TableCell>
                        ))}
                      </TableRow>
                    ))
                  ) : (
                    <TableRow>
                      <TableCell colSpan={columns.length} className="h-24 text-center">
                        No results.
                      </TableCell>
                    </TableRow>
                  )}
                </TableBody>
              </Table>
            </div>
          </CardContent>
        </Card>
      </div>
    </div>
  );
}
```

---

### 4. Real-time WebSocket Integration

```typescript
// hooks/use-realtime-chart.ts
'use client';

import { useEffect, useState, useCallback, useRef } from 'react';

interface RealtimeChartOptions {
  maxPoints?: number;
  refreshInterval?: number;
  websocketUrl?: string;
}

interface DataPoint {
  timestamp: number;
  value: number;
  [key: string]: number;
}

export function useRealtimeChart<T extends DataPoint>({
  maxPoints = 60,
  refreshInterval = 1000,
  websocketUrl,
}: RealtimeChartOptions = {}) {
  const [data, setData] = useState<T[]>([]);
  const wsRef = useRef<WebSocket | null>(null);
  const reconnectTimeoutRef = useRef<NodeJS.Timeout>();

  const addDataPoint = useCallback(
    (point: Omit<T, 'timestamp'> & { timestamp?: number }) => {
      const newPoint = {
        ...point,
        timestamp: point.timestamp ?? Date.now(),
      } as T;

      setData((prev) => {
        const updated = [...prev, newPoint];
        return updated.length > maxPoints ? updated.slice(-maxPoints) : updated;
      });
    },
    [maxPoints]
  );

  const clearData = useCallback(() => {
    setData([]);
  }, []);

  useEffect(() => {
    if (!websocketUrl) return;

    const connect = () => {
      wsRef.current = new WebSocket(websocketUrl);

      wsRef.current.onmessage = (event) => {
        try {
          const point = JSON.parse(event.data);
          addDataPoint(point);
        } catch (e) {
          console.error('Failed to parse WebSocket message:', e);
        }
      };

      wsRef.current.onclose = () => {
        reconnectTimeoutRef.current = setTimeout(connect, 3000);
      };

      wsRef.current.onerror = () => {
        wsRef.current?.close();
      };
    };

    connect();

    return () => {
      if (reconnectTimeoutRef.current) {
        clearTimeout(reconnectTimeoutRef.current);
      }
      wsRef.current?.close();
    };
  }, [websocketUrl, addDataPoint]);

  return { data, addDataPoint, clearData };
}
```

```typescript
// components/charts/realtime-dashboard.tsx
'use client';

import { useState, useEffect } from 'react';
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card';
import {
  LineChart,
  Line,
  XAxis,
  YAxis,
  CartesianGrid,
  Tooltip,
  ResponsiveContainer,
  Legend,
} from 'recharts';
import { Badge } from '@/components/ui/badge';

interface MultiMetricData {
  timestamp: number;
  cpu: number;
  memory: number;
  network: number;
  disk: number;
}

function generateMockData(): MultiMetricData {
  return {
    timestamp: Date.now(),
    cpu: Math.random() * 100,
    memory: 40 + Math.random() * 40,
    network: Math.random() * 500,
    disk: 60 + Math.random() * 20,
  };
}

export function RealtimeDashboard() {
  const [metrics, setMetrics] = useState<MultiMetricData[]>([]);
  const [connectionStatus, setConnectionStatus] = useState<'connected' | 'disconnected'>('connected');

  useEffect(() => {
    const interval = setInterval(() => {
      setMetrics((prev) => {
        const newData = [...prev, generateMockData()];
        return newData.slice(-60);
      });
    }, 1000);

    return () => clearInterval(interval);
  }, []);

  const chartData = metrics.map((m) => ({
    time: new Date(m.timestamp).toLocaleTimeString(),
    ...m,
  }));

  const currentMetrics = metrics[metrics.length - 1] || { cpu: 0, memory: 0, network: 0, disk: 0 };

  return (
    <div className="space-y-6">
      <div className="flex items-center justify-between">
        <h2 className="text-2xl font-bold">System Metrics</h2>
        <Badge variant={connectionStatus === 'connected' ? 'default' : 'destructive'}>
          {connectionStatus === 'connected' ? 'Live' : 'Disconnected'}
        </Badge>
      </div>

      <div className="grid grid-cols-2 md:grid-cols-4 gap-4">
        {[
          { label: 'CPU', value: currentMetrics.cpu, max: 100, unit: '%', color: 'bg-blue-500' },
          { label: 'Memory', value: currentMetrics.memory, max: 100, unit: '%', color: 'bg-purple-500' },
          { label: 'Network', value: currentMetrics.network, max: 500, unit: 'MB/s', color: 'bg-green-500' },
          { label: 'Disk', value: currentMetrics.disk, max: 100, unit: '%', color: 'bg-orange-500' },
        ].map((metric) => (
          <Card key={metric.label}>
            <CardContent className="pt-6">
              <div className="text-2xl font-bold">
                {metric.value.toFixed(1)}
                <span className="text-sm text-muted-foreground ml-1">{metric.unit}</span>
              </div>
              <p className="text-xs text-muted-foreground">{metric.label}</p>
              <div className="mt-2 h-2 w-full rounded-full bg-muted overflow-hidden">
                <div
                  className={`h-full ${metric.color} transition-all duration-300`}
                  style={{ width: `${(metric.value / metric.max) * 100}%` }}
                />
              </div>
            </CardContent>
          </Card>
        ))}
      </div>

      <Card>
        <CardHeader>
          <CardTitle>Real-time Metrics (60s window)</CardTitle>
        </CardHeader>
        <CardContent>
          <ResponsiveContainer width="100%" height={400}>
            <LineChart data={chartData}>
              <CartesianGrid strokeDasharray="3 3" className="stroke-muted" />
              <XAxis
                dataKey="time"
                className="text-xs"
                interval="preserveStartEnd"
                tick={{ fontSize: 10 }}
              />
              <YAxis className="text-xs" />
              <Tooltip
                contentStyle={{
                  backgroundColor: 'hsl(var(--card))',
                  border: '1px solid hsl(var(--border))',
                  borderRadius: 'var(--radius)',
                }}
              />
              <Legend />
              <Line type="monotone" dataKey="cpu" name="CPU %" stroke="#3b82f6" dot={false} />
              <Line type="monotone" dataKey="memory" name="Memory %" stroke="#a855f7" dot={false} />
              <Line type="monotone" dataKey="network" name="Network MB/s" stroke="#22c55e" dot={false} />
              <Line type="monotone" dataKey="disk" name="Disk %" stroke="#f97316" dot={false} />
            </LineChart>
          </ResponsiveContainer>
        </CardContent>
      </Card>
    </div>
  );
}
```

---

## Chart Types Guide

| Data Pattern | Best Chart | Use Case |
|--------------|------------|----------|
| Trends over time | Line, Area | Revenue, growth, stock prices |
| Comparisons (categories) | Bar, Column | Sales by region, product comparison |
| Part-to-whole | Pie, Donut, Treemap | Market share, budget allocation |
| Distributions | Histogram, Box plot | User behavior, response times |
| Correlations | Scatter | Height vs weight, price vs demand |
| Funnels | Funnel, Waterfall | Sales pipeline, conversion |
| Multi-axis | Composed | Sales vs targets vs conversion |
| Geographical | Map | Regional data, location metrics |
| Hierarchical | Tree map, Sunburst | Organizational structure |
| Relationships | Network, Sankey | User flows, dependencies |

---

## Workflow

### Step 1: Choose Library
```typescript
const selectionCriteria = {
  reactApp: 'recharts',
  nextjsSSR: 'nivo',
  saasTailwind: 'tremor',
  enterprise: 'echarts',
  maxControl: 'd3',
  quickSimple: 'chartjs',
};
```

### Step 2: Install
```bash
npm install recharts
npm install @tremor/react
npm install @tanstack/react-table
npm install chart.js react-chartjs-2
npm install echarts echarts-for-react
```

### Step 3: Create Component
Follow the patterns above based on chart type needed.

### Step 4: Integrate with Dashboard
```typescript
// layout example with responsive grid
<div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
  <KPICard title="Revenue" metric={125000} metricFormat="currency" change={12.5} />
  <KPICard title="Users" metric={8420} change={8.2} />
  <KPICard title="Conversion" metric={3.8} metricFormat="percent" change={-0.5} changeType="negative" />
</div>
```

### Step 5: Add Real-time (if needed)
```typescript
// Use the useRealtimeChart hook for live data
const { data, addDataPoint } = useRealtimeChart({ maxPoints: 60 });
```

---

## AI Integration Patterns

### Data Generation for Charts
```typescript
// utils/chart-data.ts
export function generateMockData(
  type: 'line' | 'bar' | 'pie',
  points: number = 12
): unknown[] {
  switch (type) {
    case 'line':
      return Array.from({ length: points }, (_, i) => ({
        x: `Point ${i + 1}`,
        y: Math.floor(Math.random() * 100),
      }));
    case 'bar':
      return ['A', 'B', 'C', 'D'].map((label) => ({
        name: label,
        value: Math.floor(Math.random() * 1000),
      }));
    case 'pie':
      return [
        { name: 'Category A', value: 30 },
        { name: 'Category B', value: 25 },
        { name: 'Category C', value: 20 },
        { name: 'Category D', value: 25 },
      ];
    default:
      return [];
  }
}
```

### Chart Recommendations based on Data Shape
```typescript
export function recommendChartType(data: {
  rows: number;
  columns: number;
  hasTimeSeries: boolean;
  categories: string[];
  numericColumns: string[];
}): string[] {
  const recommendations: string[] = [];

  if (data.hasTimeSeries && data.numericColumns.length > 0) {
    recommendations.push('line', 'area');
  }

  if (data.categories.length > 0 && data.numericColumns.length > 0) {
    recommendations.push('bar', 'column');
  }

  if (data.numericColumns.length === 1 && data.rows <= 10) {
    recommendations.push('pie', 'donut');
  }

  if (data.numericColumns.length >= 2 && data.rows > 20) {
    recommendations.push('scatter', 'heatmap');
  }

  return recommendations;
}
```

---

## Resources

| Resource | URL |
|----------|-----|
| Recharts | https://recharts.org |
| Tremor | https://tremor.so |
| Nivo | https://nivo.rocks |
| Chart.js | https://www.chartjs.org |
| ECharts | https://echarts.apache.org |
| D3.js | https://d3js.org |
| Observable Plot | https://observablehq.com/plot/ |
| TanStack Table | https://tanstack.com/table |
| Chart Chooser | https://datavizproject.com |
| Data Viz Catalogue | https://datavizcatalogue.com |

---

## Examples in Projects

Reference implementations:
- `.cursor/02_Skills/11_Taste_Skills/` - Dashboard patterns (minimalist-skill)
- `07_Projects/*/dashboard/` - Production dashboards
- `01_Core/04_Rules/00_Tech_Defaults.md` - Tech conventions
