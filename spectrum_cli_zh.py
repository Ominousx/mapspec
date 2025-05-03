
import pandas as pd
import matplotlib.pyplot as plt
import argparse

plt.rcParams['font.family'] = 'SimHei'  # 设置字体为SimHei以支持中文显示
# === CLI ARGUMENT PARSER ===
parser = argparse.ArgumentParser(description="从狼队视角生成地图自信度频谱")
parser.add_argument('--wolves', type=str, default='wolves.csv', help='狼队 CSV 文件的路径')
parser.add_argument('--opponent', type=str, required=True, help='对手 CSV 文件的路径')
parser.add_argument('--output', type=str, default='map_confidence_spectrum.png', help='输出的图片文件名')
args = parser.parse_args()

# === SCORING FUNCTION ===
def calculate_score(wins, losses, picks, bans):
    total_games = wins + losses
    win_rate = wins / total_games if total_games > 0 else 0
    score = (win_rate * 5) + (picks * 0.5) - (bans * 0.25)
    return score

# === READ DATA ===
wolves_df = pd.read_csv(args.wolves)
opponent_df = pd.read_csv(args.opponent)

# === CALCULATE CONFIDENCE ===
map_scores = {}
for i in range(len(wolves_df)):
    map_name = wolves_df.loc[i, 'Map']
    
    w_wins = wolves_df.loc[i, 'Wins']
    w_losses = wolves_df.loc[i, 'Losses']
    w_picks = wolves_df.loc[i, 'Picks']
    w_bans = wolves_df.loc[i, 'Bans']
    
    o_row = opponent_df[opponent_df['Map'] == map_name].iloc[0]
    o_wins = o_row['Wins']
    o_losses = o_row['Losses']
    o_picks = o_row['Picks']
    o_bans = o_row['Bans']
    
    w_score = calculate_score(w_wins, w_losses, w_picks, w_bans)
    o_score = calculate_score(o_wins, o_losses, o_picks, o_bans)
    
    confidence = w_score - o_score
    map_scores[map_name] = confidence

# === SORT AND NORMALIZE SCORES TO RANKS 1-7 ===
sorted_maps = sorted(map_scores.items(), key=lambda x: x[1])
ranked_maps = {name: rank+1 for rank, (name, _) in enumerate(sorted_maps)}
ordered_maps = [x[0] for x in sorted_maps]

# === COLOR SCHEME ===
colors = {
    1: "#ff4c4c",  # worst
    2: "#ff9999",
    3: "#ffcccc",
    4: "#ffffff",  # neutral
    5: "#ccffcc",
    6: "#99ff99",
    7: "#4cff4c"   # best
}
map_colors = [colors[ranked_maps[m]] for m in ordered_maps]

# === PLOT ===
fig, ax = plt.subplots(figsize=(12, 2))
for i, (map_name, color) in enumerate(zip(ordered_maps, map_colors)):
    ax.add_patch(plt.Rectangle((i, 0), 1, 1, color=color))
    ax.text(i + 0.5, 0.5, map_name, va='center', ha='center', fontsize=10, weight='bold')

ax.set_xlim(0, 7)
ax.set_ylim(0, 1)
ax.axis('off')
plt.title("地图自信度频谱 （WOL 视角）", fontsize=14, weight='bold')
plt.tight_layout()
plt.savefig(args.output, dpi=300)
plt.show()
