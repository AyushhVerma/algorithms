#include <bits/stdc++.h>
using namespace std;
#define pb push_back

stack<int> ss;

void dfs(int s, vector<int> adj[], vector<bool> &visited) {
    visited[s] = true;
    ss.push(s);
    for (auto u : adj[s]) {
        if (!visited[u])
            dfs(u, adj, visited);
    }
}

void bfs(int s, vector<int> adj[], vector<bool> &visited) {
    queue<int> q;
    q.push(s);
    visited[s] = true;
    while (!q.empty()) {
        int node = q.front();
        ss.push(node);
        q.pop();
        for (auto u : adj[node]) {
            if (!visited[u])
                q.push(u);
        }
    }
}

int main() {
    int N = 5;
    vector<int> adj[N];
    vector<bool> visited(N, false);
    adj[1].pb(2);
    adj[2].pb(3);
    adj[2].pb(4);
    adj[3].pb(4);
    adj[4].pb(1);
    // dfs(1, adj, visited);
    // bfs(1, adj, visited);
    while (!ss.empty()) { 
        cout << ss.top() << endl;
        ss.pop();
    }
    return 0;
}
