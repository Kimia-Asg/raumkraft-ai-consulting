"""
Dashboard Blueprint — Visual reference for building in Tableau.
Each figure = one Tableau dashboard tab.
"""

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np
from matplotlib.gridspec import GridSpec

# --- Setup ---
plt.rcParams.update({
    'font.family': 'sans-serif',
    'font.size': 10,
    'axes.titlesize': 14,
    'axes.titleweight': 'bold',
    'axes.spines.top': False,
    'axes.spines.right': False,
    'figure.facecolor': '#F5F7FA',
    'axes.facecolor': '#FFFFFF',
})

NAVY = '#065A82'
TEAL = '#1C7293'
MIDNIGHT = '#21295C'
GREEN = '#059669'
AMBER = '#D97706'
GRAY = '#6B7280'
LIGHT = '#E8F4F8'
PALETTE = [NAVY, TEAL, '#2D9CDB', GREEN, AMBER, '#8B5CF6']

# --- Load Data ---
properties = pd.read_csv('/home/claude/capstone-round1/data/properties.csv')
enquiries = pd.read_csv('/home/claude/capstone-round1/data/enquiries.csv')
projects = pd.read_csv('/home/claude/capstone-round1/data/projects.csv')
agents = pd.read_csv('/home/claude/capstone-round1/data/agents.csv')
revenue = pd.read_csv('/home/claude/capstone-round1/data/revenue_monthly.csv')

properties['listed_date'] = pd.to_datetime(properties['listed_date'])
properties['listed_month'] = properties['listed_date'].dt.to_period('M').astype(str)
enquiries['date'] = pd.to_datetime(enquiries['date'])
enquiries['month'] = enquiries['date'].dt.to_period('M').astype(str)

# ============================================================
# TAB 1: BUSINESS OVERVIEW
# ============================================================
fig = plt.figure(figsize=(16, 10))
fig.suptitle('Tab 1: Business Overview', fontsize=20, fontweight='bold', color=MIDNIGHT, y=0.98)
gs = GridSpec(2, 3, figure=fig, hspace=0.35, wspace=0.3,
             left=0.06, right=0.96, top=0.91, bottom=0.06)

# Revenue by service line
ax1 = fig.add_subplot(gs[0, 0:2])
rev_total = revenue.groupby('service_line')['revenue_eur'].sum().sort_values(ascending=True)
bars = ax1.barh(rev_total.index, rev_total.values / 1e6, color=[TEAL, NAVY, AMBER])
ax1.set_xlabel('Total Revenue (€ millions)')
ax1.set_title('Revenue by Service Line (2 years)')
for bar, val in zip(bars, rev_total.values):
    ax1.text(bar.get_width() + 0.05, bar.get_y() + bar.get_height()/2,
             f'€{val/1e6:.1f}M', va='center', fontsize=11, fontweight='bold', color=MIDNIGHT)

# KPI cards
ax_kpi1 = fig.add_subplot(gs[0, 2])
ax_kpi1.axis('off')
active_projects = len(projects[projects['status'] == 'Active'])
ax_kpi1.text(0.5, 0.65, str(active_projects), ha='center', va='center',
             fontsize=52, fontweight='bold', color=NAVY, transform=ax_kpi1.transAxes)
ax_kpi1.text(0.5, 0.35, 'Active Design\nProjects', ha='center', va='center',
             fontsize=13, color=GRAY, transform=ax_kpi1.transAxes)
ax_kpi1.add_patch(plt.Rectangle((0.05, 0.1), 0.9, 0.8, fill=True,
                                facecolor=LIGHT, edgecolor=NAVY, linewidth=1.5,
                                transform=ax_kpi1.transAxes, zorder=0))

# Listings per month
ax2 = fig.add_subplot(gs[1, 0:2])
listings_monthly = properties.groupby('listed_month').size()
# Take last 12 months for readability
last_12 = listings_monthly.tail(12)
ax2.plot(range(len(last_12)), last_12.values, color=NAVY, linewidth=2.5, marker='o', markersize=5)
ax2.fill_between(range(len(last_12)), last_12.values, alpha=0.1, color=NAVY)
ax2.set_xticks(range(len(last_12)))
ax2.set_xticklabels([m[-5:] for m in last_12.index], rotation=45, ha='right', fontsize=8)
ax2.set_title('Listings Published per Month (Last 12 Months)')
ax2.set_ylabel('Count')

# Total enquiries KPI
ax_kpi2 = fig.add_subplot(gs[1, 2])
ax_kpi2.axis('off')
total_enquiries = len(enquiries)
ax_kpi2.text(0.5, 0.65, f'{total_enquiries:,}', ha='center', va='center',
             fontsize=44, fontweight='bold', color=TEAL, transform=ax_kpi2.transAxes)
ax_kpi2.text(0.5, 0.35, 'Total Enquiries\n(2 years)', ha='center', va='center',
             fontsize=13, color=GRAY, transform=ax_kpi2.transAxes)
ax_kpi2.add_patch(plt.Rectangle((0.05, 0.1), 0.9, 0.8, fill=True,
                                facecolor=LIGHT, edgecolor=TEAL, linewidth=1.5,
                                transform=ax_kpi2.transAxes, zorder=0))

fig.savefig('/home/claude/capstone-round1/dashboard/blueprint_tab1_overview.png', dpi=150, bbox_inches='tight')
plt.close()
print("Tab 1 done")

# ============================================================
# TAB 2: LISTING PERFORMANCE
# ============================================================
fig = plt.figure(figsize=(16, 10))
fig.suptitle('Tab 2: Listing Performance', fontsize=20, fontweight='bold', color=MIDNIGHT, y=0.98)
gs = GridSpec(2, 2, figure=fig, hspace=0.35, wspace=0.3,
             left=0.06, right=0.96, top=0.91, bottom=0.06)

# Histogram: days to publish
ax1 = fig.add_subplot(gs[0, 0])
ax1.hist(properties['days_to_publish'], bins=20, color=NAVY, edgecolor='white', alpha=0.85)
ax1.axvline(properties['days_to_publish'].mean(), color=AMBER, linestyle='--', linewidth=2,
            label=f'Mean: {properties["days_to_publish"].mean():.1f} days')
ax1.set_title('Days to Publish (Distribution)')
ax1.set_xlabel('Days')
ax1.set_ylabel('Count')
ax1.legend()

# Property type breakdown
ax2 = fig.add_subplot(gs[0, 1])
type_counts = properties['property_type'].value_counts()
colors = [NAVY, TEAL, '#2D9CDB', AMBER, GREEN]
wedges, texts, autotexts = ax2.pie(type_counts, labels=type_counts.index,
                                    autopct='%1.0f%%', colors=colors,
                                    startangle=90, pctdistance=0.8)
for t in autotexts:
    t.set_fontsize(10)
    t.set_fontweight('bold')
ax2.set_title('Listings by Property Type')

# Agent productivity
ax3 = fig.add_subplot(gs[1, 0:2])
agent_sorted = agents.sort_values('avg_days_to_publish', ascending=False).head(20)
colors_bar = [AMBER if v > 12 else NAVY for v in agent_sorted['avg_days_to_publish']]
ax3.barh(agent_sorted['name'], agent_sorted['avg_days_to_publish'], color=colors_bar)
ax3.axvline(7, color=GREEN, linestyle='--', linewidth=2, label='Target: 7 days')
ax3.set_title('Avg Days to Publish by Agent (Top 20 — amber = above 12 days)')
ax3.set_xlabel('Days')
ax3.legend()
ax3.invert_yaxis()

fig.savefig('/home/claude/capstone-round1/dashboard/blueprint_tab2_listings.png', dpi=150, bbox_inches='tight')
plt.close()
print("Tab 2 done")

# ============================================================
# TAB 3: CLIENT ENQUIRY ANALYSIS
# ============================================================
fig = plt.figure(figsize=(16, 10))
fig.suptitle('Tab 3: Client Enquiry Analysis', fontsize=20, fontweight='bold', color=MIDNIGHT, y=0.98)
gs = GridSpec(2, 2, figure=fig, hspace=0.35, wspace=0.3,
             left=0.06, right=0.96, top=0.91, bottom=0.06)

# Enquiry volume by channel (stacked)
ax1 = fig.add_subplot(gs[0, 0:2])
pivot = enquiries.groupby(['month', 'channel']).size().unstack(fill_value=0)
pivot_last12 = pivot.tail(12)
pivot_last12.plot(kind='bar', stacked=True, ax=ax1, color=[NAVY, TEAL, '#2D9CDB', AMBER], width=0.8)
ax1.set_title('Enquiry Volume by Channel (Last 12 Months)')
ax1.set_xlabel('')
ax1.set_xticklabels([m[-5:] for m in pivot_last12.index], rotation=45, ha='right', fontsize=8)
ax1.legend(title='Channel', bbox_to_anchor=(1.0, 1.0))
ax1.set_ylabel('Count')

# Enquiry type breakdown
ax2 = fig.add_subplot(gs[1, 0])
eq_types = enquiries['enquiry_type'].value_counts()
colors_eq = [NAVY, TEAL, '#2D9CDB', AMBER, GREEN, '#EF4444']
ax2.barh(eq_types.index, eq_types.values, color=colors_eq)
ax2.set_title('Enquiries by Type')
ax2.set_xlabel('Count')

# Auto-draftable highlight
auto_types = ['Viewing Request', 'Pricing Question', 'Availability Check']
auto_pct = enquiries[enquiries['enquiry_type'].isin(auto_types)].shape[0] / len(enquiries) * 100

# Response time trend
ax3 = fig.add_subplot(gs[1, 1])
resp_monthly = enquiries.groupby('month')['response_time_hours'].mean().tail(12)
ax3.plot(range(len(resp_monthly)), resp_monthly.values, color=NAVY, linewidth=2.5, marker='o', markersize=4)
ax3.axhline(2, color=GREEN, linestyle='--', linewidth=2, label='Target: 2 hours')
ax3.fill_between(range(len(resp_monthly)), resp_monthly.values, 2,
                 where=resp_monthly.values > 2, alpha=0.15, color=AMBER)
ax3.set_title(f'Avg Response Time (Target: 2h)')
ax3.set_xticks(range(len(resp_monthly)))
ax3.set_xticklabels([m[-5:] for m in resp_monthly.index], rotation=45, ha='right', fontsize=8)
ax3.set_ylabel('Hours')
ax3.legend()

fig.savefig('/home/claude/capstone-round1/dashboard/blueprint_tab3_enquiries.png', dpi=150, bbox_inches='tight')
plt.close()
print("Tab 3 done")

# ============================================================
# TAB 4: AI OPPORTUNITY INDICATORS
# ============================================================
fig = plt.figure(figsize=(16, 8))
fig.suptitle('Tab 4: AI Opportunity Indicators', fontsize=20, fontweight='bold', color=MIDNIGHT, y=0.98)
gs = GridSpec(1, 4, figure=fig, wspace=0.3,
             left=0.04, right=0.96, top=0.85, bottom=0.1)

kpis = [
    {'val': f'{properties.shape[0] * 0.5:.0f}h', 'label': 'Hours Saved\non Listings/Year',
     'sub': f'{properties.shape[0]} listings × 30 min', 'color': GREEN},
    {'val': f'{auto_pct:.0f}%', 'label': 'Enquiries Eligible\nfor Auto-Draft',
     'sub': f'{auto_pct:.0f}% routine types', 'color': NAVY},
    {'val': f'{projects["brief_hours"].sum():.0f}h', 'label': 'Brief Hours\nSaveable/Year',
     'sub': f'{len(projects)} projects × avg {projects["brief_hours"].mean():.1f}h', 'color': TEAL},
    {'val': '~1 mo', 'label': 'Payback\nPeriod', 'sub': '€12-15k upfront → €15-31k/mo value', 'color': AMBER},
]

for i, kpi in enumerate(kpis):
    ax = fig.add_subplot(gs[0, i])
    ax.axis('off')
    ax.add_patch(plt.Rectangle((0.02, 0.02), 0.96, 0.96, fill=True,
                                facecolor='white', edgecolor=kpi['color'],
                                linewidth=2, transform=ax.transAxes,
                                zorder=0))
    ax.text(0.5, 0.7, kpi['val'], ha='center', va='center',
            fontsize=38, fontweight='bold', color=kpi['color'],
            transform=ax.transAxes)
    ax.text(0.5, 0.4, kpi['label'], ha='center', va='center',
            fontsize=12, fontweight='bold', color=MIDNIGHT,
            transform=ax.transAxes)
    ax.text(0.5, 0.15, kpi['sub'], ha='center', va='center',
            fontsize=9, color=GRAY, transform=ax.transAxes)

fig.savefig('/home/claude/capstone-round1/dashboard/blueprint_tab4_opportunity.png', dpi=150, bbox_inches='tight')
plt.close()
print("Tab 4 done")
print("\nAll blueprints saved!")
