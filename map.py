# # # # import streamlit as st
# # # # import folium
# # # # from streamlit_folium import folium_static

# # # # # Set the initial location and zoom level for the map
# # # # map_center = [37.7749, -122.4194]  # San Francisco coordinates
# # # # m = folium.Map(location=map_center, zoom_start=13)

# # # # # Add a marker to the map
# # # # folium.Marker(map_center, tooltip='San Francisco').add_to(m)

# # # # # Display the map in the Streamlit app
# # # # st.title('2D Map with Folium')
# # # # folium_static(m)



# # # import streamlit as st
# # # import plotly.graph_objects as go

# # # # Define the dimensions of your world map
# # # world_width = 100
# # # world_height = 100

# # # # Define the robots and their start/end points
# # # robots = {
# # #     'Robot 1': {'start': (10, 20), 'end': (80, 70), 'color': 'red'},
# # #     'Robot 2': {'start': (20, 30), 'end': (60, 90), 'color': 'blue'},
# # #     'Robot 3': {'start': (30, 40), 'end': (50, 60), 'color': 'green'}
# # # }

# # # # Create a Plotly figure
# # # fig = go.Figure()

# # # # Add robots' start and end points to the figure
# # # for robot, data in robots.items():
# # #     start = data['start']
# # #     end = data['end']
# # #     color = data['color']
    
# # #     fig.add_trace(go.Scatter(
# # #         x=[start[0], end[0]],
# # #         y=[start[1], end[1]],
# # #         mode='markers+lines',
# # #         marker=dict(symbol='diamond', size=10, color=color),
# # #         line=dict(color=color, width=2),
# # #         name=robot
# # #     ))

# # # # Set figure layout
# # # fig.update_layout(
# # #     title='Custom World Map with Robots',
# # #     xaxis_title='X Coordinate',
# # #     yaxis_title='Y Coordinate',
# # #     xaxis=dict(range=[0, world_width]),
# # #     yaxis=dict(range=[0, world_height]),
# # #     showlegend=True
# # # )

# # # # Display the figure in the Streamlit app
# # # st.title('Custom World Map with Robots')
# # # st.plotly_chart(fig)


# # import streamlit as st
# # import folium
# # import time
# # from streamlit_folium import folium_static

# # # Create a map centered on some location
# # m = folium.Map(location=[45.5236, -122.6750], zoom_start=13)

# # # Define robots with start and end points
# # robots = {
# #     'Robot 1': {'start': [45.5236, -122.6750], 'end': [45.5289, -122.6800], 'color': 'red'},
# #     'Robot 2': {'start': [45.5244, -122.6762], 'end': [45.5295, -122.6812], 'color': 'blue'},
# #     'Robot 3': {'start': [45.5228, -122.6748], 'end': [45.5278, -122.6798], 'color': 'green'}
# # }

# # # Define a function to move the robots
# # def move_robot(robot, start, end, steps=10):
# #     lat_step = (end[0] - start[0]) / steps
# #     lon_step = (end[1] - start[1]) / steps
# #     positions = []
# #     for i in range(steps + 1):
# #         lat = start[0] + i * lat_step
# #         lon = start[1] + i * lon_step
# #         positions.append((lat, lon))
# #     return positions

# # # Initialize robot positions
# # robot_positions = {robot: move_robot(robot, data['start'], data['end']) for robot, data in robots.items()}

# # # Display the initial map
# # st.title('Custom World Map with Robots')
# # folium_static(m)

# # # Add a chat box
# # st.subheader("Robot Communication")
# # chat_box = st.empty()

# # # Simulate robot movement
# # steps = len(list(robot_positions.values())[0])
# # for step in range(steps):
# #     # Clear previous markers
# #     m = folium.Map(location=[45.5236, -122.6750], zoom_start=13)

# #     for robot, positions in robot_positions.items():
# #         lat, lon = positions[step]
# #         folium.Marker(
# #             location=[lat, lon],
# #             icon=folium.Icon(color=robots[robot]['color'], icon='info-sign')
# #         ).add_to(m)

# #         # Simulate a message from the robot
# #         chat_box.text(f"{robot} moved to {lat:.4f}, {lon:.4f}")

# #     # Update the map
# #     folium_static(m)

# #     # Wait for a while to simulate real-time movement
# #     time.sleep(1)





# V1 works
# import streamlit as st
# import matplotlib.pyplot as plt
# import numpy as np
# import time

# # Define the robot's path
# path = [
#     (0, 0), (5, 5), (10, 10), (11, 12), (13, 17), (15, 18), (18, 19), (20, 20)
# ]
# messages = {
#     (10, 10): "Reached checkpoint (10, 10).",
#     (13, 17): "Reached checkpoint (13, 17)."
# }

# # Function to create the grid map
# def create_map(center, robot_position):
#     fig, ax = plt.subplots()
#     ax.set_xlim(center[0] - 15, center[0] + 15)
#     ax.set_ylim(center[1] - 15, center[1] + 15)
    
#     # Draw grid
#     for i in range(51):
#         ax.axhline(i, color='lightgrey', linewidth=0.5)
#         ax.axvline(i, color='lightgrey', linewidth=0.5)

#     # Plot the robot's path
#     path_x, path_y = zip(*path)
#     ax.plot(path_x, path_y, marker='o', markersize=5, color='blue', linestyle='--')

#     # Plot the robot's current position
#     ax.plot(robot_position[0], robot_position[1], marker='D', markersize=10, color='red')

#     return fig

# # Streamlit interface
# st.title("Custom World Map with Robots")

# # Initialize robot's starting position
# robot_position = path[0]

# # Initialize chat box
# chat_box = st.empty()

# # Simulate robot movement
# for position in path:
#     robot_position = position
#     center = robot_position

#     # Create and display the map
#     fig = create_map(center, robot_position)
#     st.pyplot(fig)

#     # Display communication messages
#     if robot_position in messages:
#         chat_box.text(messages[robot_position])

#     # Wait for a while to simulate real-time movement
#     time.sleep(1)


# import streamlit as st
# import plotly.graph_objects as go
# import time

# # Define the robot's path
# path = [
#     (0, 0), (5, 5), (10, 10), (11, 12), (13, 17), (15, 18), (18, 19), (20, 20)
# ]
# messages = {
#     (10, 10): "Reached checkpoint (10, 10).",
#     (13, 17): "Reached checkpoint (13, 17)."
# }

# # Create a Plotly figure for the map
# fig = go.Figure()

# # Add the grid lines
# for i in range(0, 51, 1):
#     fig.add_trace(go.Scatter(x=[i, i], y=[0, 50], mode='lines', line=dict(color='lightgrey', width=0.5), showlegend=False))
#     fig.add_trace(go.Scatter(x=[0, 50], y=[i, i], mode='lines', line=dict(color='lightgrey', width=0.5), showlegend=False))

# # Add the robot's path
# path_x, path_y = zip(*path)
# fig.add_trace(go.Scatter(x=path_x, y=path_y, mode='lines+markers', line=dict(color='blue', dash='dash'), marker=dict(size=5), name='Path'))

# # Initialize the robot's starting position
# robot_position = path[0]
# robot_trace = go.Scatter(x=[robot_position[0]], y=[robot_position[1]], mode='markers', marker=dict(symbol='diamond', size=10, color='red'), name='Robot')
# fig.add_trace(robot_trace)

# # Set figure layout
# fig.update_layout(
#     title='Custom World Map with Robots',
#     xaxis=dict(range=[0, 50], autorange=False),
#     yaxis=dict(range=[0, 50], autorange=False),
#     width=600,
#     height=600,
#     showlegend=True
# )

# # Streamlit interface
# st.title("Custom World Map with Robots")
# map_placeholder = st.empty()
# chat_placeholder = st.empty()

# # Simulate robot movement
# for position in path:
#     robot_position = position

#     # Update the robot's position
#     fig.data[-1].x = [robot_position[0]]
#     fig.data[-1].y = [robot_position[1]]
    
#     # Display the updated map
#     with map_placeholder:
#         st.plotly_chart(fig)

#     # Display communication messages
#     if robot_position in messages:
#         with chat_placeholder:
#             st.text(messages[robot_position])
    
#     # Wait for a while to simulate real-time movement
#     time.sleep(1)



# #ideal 1 robot
# import streamlit as st
# import plotly.graph_objects as go
# import time

# # Define the robot's path
# path = [
#     (0, 0), (5, 5), (10, 10), (11, 12), (13, 17), (15, 18), (18, 19), (20, 20)
# ]
# messages = {
#     (10, 10): "Reached checkpoint (10, 10).",
#     (13, 17): "Reached checkpoint (13, 17)."
# }

# # Create a Plotly figure for the map
# fig = go.Figure()

# # Add the grid lines
# for i in range(0, 51, 1):
#     fig.add_trace(go.Scatter(x=[i, i], y=[0, 50], mode='lines', line=dict(color='lightgrey', width=0.5), showlegend=False))
#     fig.add_trace(go.Scatter(x=[0, 50], y=[i, i], mode='lines', line=dict(color='lightgrey', width=0.5), showlegend=False))

# # Add the robot's path
# path_x, path_y = zip(*path)
# fig.add_trace(go.Scatter(x=path_x, y=path_y, mode='lines+markers', line=dict(color='blue', dash='dash'), marker=dict(size=5), name='Path'))

# # Initialize the robot's starting position
# robot_position = path[0]
# robot_trace = go.Scatter(x=[robot_position[0]], y=[robot_position[1]], mode='markers', marker=dict(symbol='diamond', size=10, color='red'), name='Robot')
# fig.add_trace(robot_trace)

# # Set figure layout
# fig.update_layout(
#     title='Custom World Map with Robots',
#     xaxis=dict(range=[0, 50], autorange=False),
#     yaxis=dict(range=[0, 50], autorange=False),
#     width=600,
#     height=600,
#     showlegend=True
# )

# # Streamlit interface
# st.title("Custom World Map with Robots")
# map_placeholder = st.empty()
# chat_placeholder = st.empty()

# # Simulate robot movement
# for position in path:
#     robot_position = position

#     # Update the robot's position
#     fig.data[-1].x = [robot_position[0]]
#     fig.data[-1].y = [robot_position[1]]
    
#     # Display the updated map
#     with map_placeholder:
#         st.plotly_chart(fig)

#     # Display communication messages
#     if robot_position in messages:
#         with chat_placeholder:
#             st.text(messages[robot_position])
#     else:
#         with chat_placeholder:
#             st.empty()
    
#     # Wait for a while to simulate real-time movement
#     time.sleep(1)



# import streamlit as st
# import plotly.graph_objects as go
# import time
# import random

# # Define the robots' paths and messages
# robots = {
#     'Explorer Robot': {
#         'path': [(0, 0), (5, 5), (10, 10), (12, 12), (15, 15)],
#         'color': 'blue',
#         'messages': {
#             (10, 10): "Explorer Robot reached checkpoint (10, 10).",
#             (15, 15): "Explorer Robot reached destination (15, 15)."
#         }
#     },
#     'Scout Robot': {
#         'path': [(2, 2), (6, 8), (12, 10), (15, 12), (18, 15)],
#         'color': 'green',
#         'messages': {
#             (6, 8): "Scout Robot reached checkpoint (6, 8).",
#             (18, 15): "Scout Robot reached destination (18, 15)."
#         }
#     },
#     'Surveyor Robot': {
#         'path': [(1, 1), (7, 3), (12, 5), (16, 8), (20, 10)],
#         'color': 'red',
#         'messages': {
#             (7, 3): "Surveyor Robot reached checkpoint (7, 3).",
#             (16, 8): "Surveyor Robot reached checkpoint (16, 8)."
#         }
#     },
#     'Drone Robot': {
#         'path': [(3, 3), (8, 6), (12, 9), (15, 12), (20, 18)],
#         'color': 'purple',
#         'messages': {
#             (8, 6): "Drone Robot reached checkpoint (8, 6).",
#             (15, 12): "Drone Robot reached checkpoint (15, 12).",
#             (20, 18): "Drone Robot reached destination (20, 18)."
#         }
#     }
# }

# # Create a Plotly figure for the map
# fig = go.Figure()

# # Add the grid lines
# for i in range(0, 51, 1):
#     fig.add_trace(go.Scatter(x=[i, i], y=[0, 50], mode='lines', line=dict(color='lightgrey', width=0.5), showlegend=False))
#     fig.add_trace(go.Scatter(x=[0, 50], y=[i, i], mode='lines', line=dict(color='lightgrey', width=0.5), showlegend=False))

# # Add each robot's path and marker
# for robot_name, robot_data in robots.items():
#     path = robot_data['path']
#     color = robot_data['color']
#     messages = robot_data['messages']
    
#     path_x, path_y = zip(*path)
#     fig.add_trace(go.Scatter(x=path_x, y=path_y, mode='lines+markers', line=dict(color=color, dash='dash'), marker=dict(size=5), name=f'{robot_name} Path'))

#     # Add the robot's starting position
#     robot_position = path[0]
#     fig.add_trace(go.Scatter(x=[robot_position[0]], y=[robot_position[1]], mode='markers', marker=dict(symbol='diamond', size=10, color=color), name=f'{robot_name}'))

# # Set figure layout
# fig.update_layout(
#     title='Custom World Map with Robots',
#     xaxis=dict(range=[0, 50], autorange=False),
#     yaxis=dict(range=[0, 50], autorange=False),
#     width=800,
#     height=800,
#     showlegend=True
# )

# # Streamlit interface
# st.title("Custom World Map with Robots")
# map_placeholder = st.empty()
# chat_placeholder = st.empty()

# # Simulate robot movements
# while True:
#     for robot_name, robot_data in robots.items():
#         path = robot_data['path']
#         color = robot_data['color']
#         messages = robot_data['messages']

#         for position in path:
#             # Update the robot's position
#             fig.data[-len(robots) + list(robots.keys()).index(robot_name)].x = [position[0]]
#             fig.data[-len(robots) + list(robots.keys()).index(robot_name)].y = [position[1]]

#             # Display the updated map
#             with map_placeholder:
#                 st.plotly_chart(fig)

#             # Display communication messages
#             if position in messages:
#                 with chat_placeholder:
#                     st.text(messages[position])
#             else:
#                 with chat_placeholder:
#                     st.empty()

#             # Wait for a while to simulate real-time movement
#             time.sleep(1)




# import streamlit as st
# import plotly.graph_objects as go
# import time
# import random

# def generate_random_path(start, end, min_steps=8, max_steps=15):
#     # Create a path with random steps between start and end points
#     num_steps = random.randint(min_steps, max_steps)
#     x_start, y_start = start
#     x_end, y_end = end
    
#     x_steps = [x_start]
#     y_steps = [y_start]
    
#     for _ in range(num_steps - 1):
#         x_step = x_steps[-1] + random.choice([-1, 0, 1])
#         y_step = y_steps[-1] + random.choice([-1, 0, 1])
#         x_step = min(max(x_step, 0), 50)  # Ensure within bounds
#         y_step = min(max(y_step, 0), 50)  # Ensure within bounds
#         x_steps.append(x_step)
#         y_steps.append(y_step)
    
#     x_steps.append(x_end)
#     y_steps.append(y_end)
    
#     return list(zip(x_steps, y_steps))

# def generate_random_start_end():
#     x_start = random.randint(0, 50)
#     y_start = random.randint(0, 50)
#     x_end = random.randint(0, 50)
#     y_end = random.randint(0, 50)
#     return (x_start, y_start), (x_end, y_end)

# # Define the robots' initial data
# robots = {
#     'Explorer Robot': {
#         'color': 'blue',
#         'start_end': generate_random_start_end(),
#         'messages': {
#             (random.randint(0, 50), random.randint(0, 50)): "Explorer Robot reached checkpoint."
#         }
#     },
#     'Scout Robot': {
#         'color': 'green',
#         'start_end': generate_random_start_end(),
#         'messages': {
#             (random.randint(0, 50), random.randint(0, 50)): "Scout Robot reached checkpoint."
#         }
#     },
#     'Surveyor Robot': {
#         'color': 'orange',
#         'start_end': generate_random_start_end(),
#         'messages': {
#             (random.randint(0, 50), random.randint(0, 50)): "Surveyor Robot reached checkpoint."
#         }
#     },
#     'Drone Robot': {
#         'color': 'purple',
#         'start_end': generate_random_start_end(),
#         'messages': {
#             (random.randint(0, 50), random.randint(0, 50)): "Drone Robot reached checkpoint."
#         }
#     }
# }

# # Create a Plotly figure for the map
# fig = go.Figure()

# # Add the grid lines
# for i in range(0, 51, 1):
#     fig.add_trace(go.Scatter(x=[i, i], y=[0, 50], mode='lines', line=dict(color='lightgrey', width=0.5), showlegend=False))
#     fig.add_trace(go.Scatter(x=[0, 50], y=[i, i], mode='lines', line=dict(color='lightgrey', width=0.5), showlegend=False))

# # Initialize robot traces
# robot_traces = {}
# for robot_name, robot_data in robots.items():
#     start, end = robot_data['start_end']
#     path = generate_random_path(start, end)
    
#     robot_trace = go.Scatter(x=[start[0]], y=[start[1]], mode='markers', marker=dict(symbol='diamond', size=10, color=robot_data['color']), name=f'{robot_name}')
#     fig.add_trace(robot_trace)
    
#     robot_traces[robot_name] = {
#         'trace': robot_trace,
#         'path': path,
#         'current_index': 0,
#         'messages': robot_data['messages']
#     }

# # Set figure layout
# fig.update_layout(
#     title='Custom World Map with Robots',
#     xaxis=dict(range=[0, 50], autorange=False),
#     yaxis=dict(range=[0, 50], autorange=False),
#     width=800,
#     height=800,
#     showlegend=True
# )

# # Streamlit interface
# st.title("Custom World Map with Robots")
# map_placeholder = st.empty()
# chat_placeholder = st.empty()

# # Simulate robot movement
# while True:
#     for robot_name, robot_data in robot_traces.items():
#         if robot_data['current_index'] < len(robot_data['path']):
#             position = robot_data['path'][robot_data['current_index']]
#             robot_data['trace'].x = [position[0]]
#             robot_data['trace'].y = [position[1]]
            
#             # Update index for next step
#             robot_data['current_index'] += 1
            
#             # Display the updated map
#             with map_placeholder:
#                 st.plotly_chart(fig)
            
#             # Display communication messages
#             if position in robot_data['messages']:
#                 with chat_placeholder:
#                     st.text(robot_data['messages'][position])
#             else:
#                 with chat_placeholder:
#                     st.empty()
    
#     # Wait for a while to simulate real-time movement
#     time.sleep(1)



# import streamlit as st
# import plotly.graph_objects as go
# import time
# import random

# def generate_random_path(start, end, min_steps=8, max_steps=15):
#     num_steps = random.randint(min_steps, max_steps)
#     x_start, y_start = start
#     x_end, y_end = end
    
#     x_steps = [x_start]
#     y_steps = [y_start]
    
#     for _ in range(num_steps - 1):
#         x_step = x_steps[-1] + random.choice([-1, 0, 1])
#         y_step = y_steps[-1] + random.choice([-1, 0, 1])
#         x_step = min(max(x_step, 0), 50)  # Ensure within bounds
#         y_step = min(max(y_step, 0), 50)  # Ensure within bounds
#         x_steps.append(x_step)
#         y_steps.append(y_step)
    
#     x_steps.append(x_end)
#     y_steps.append(y_end)
    
#     return list(zip(x_steps, y_steps))

# def generate_random_start_end():
#     x_start = random.randint(0, 50)
#     y_start = random.randint(0, 50)
#     x_end = random.randint(0, 50)
#     y_end = random.randint(0, 50)
#     return (x_start, y_start), (x_end, y_end)

# # Define the robots' initial data
# robots = {
#     'Explorer Robot': {
#         'color': 'blue',
#         'start_end': generate_random_start_end(),
#     },
#     'Scout Robot': {
#         'color': 'green',
#         'start_end': generate_random_start_end(),
#     },
#     'Surveyor Robot': {
#         'color': 'orange',
#         'start_end': generate_random_start_end(),
#     },
#     'Drone Robot': {
#         'color': 'purple',
#         'start_end': generate_random_start_end(),
#     }
# }

# # Create a Plotly figure for the map
# fig = go.Figure()

# # Add the grid lines
# for i in range(0, 51, 1):
#     fig.add_trace(go.Scatter(x=[i, i], y=[0, 50], mode='lines', line=dict(color='lightgrey', width=0.5), showlegend=False))
#     fig.add_trace(go.Scatter(x=[0, 50], y=[i, i], mode='lines', line=dict(color='lightgrey', width=0.5), showlegend=False))

# # Initialize robot traces and paths
# robot_traces = {}
# for robot_name, robot_data in robots.items():
#     start, end = robot_data['start_end']
#     path = generate_random_path(start, end)
#     path_x, path_y = zip(*path)
    
#     # Add the full path for each robot
#     fig.add_trace(go.Scatter(x=path_x, y=path_y, mode='lines', line=dict(color=robot_data['color'], dash='dash'), name=f'{robot_name} Path'))
    
#     # Initialize the robot's trace
#     robot_trace = go.Scatter(x=[start[0]], y=[start[1]], mode='markers', marker=dict(symbol='diamond', size=10, color=robot_data['color']), name=f'{robot_name}')
#     fig.add_trace(robot_trace)
    
#     # Generate messages
#     checkpoints = path[1:-1]  # Exclude start and end points
#     messages = {point: f"Alert! {robot_name} has reached {point} later than expected!" for point in checkpoints}
    
#     robot_traces[robot_name] = {
#         'trace': robot_trace,
#         'path': path,
#         'current_index': 0,
#         'messages': messages
#     }

# # Set figure layout
# fig.update_layout(
#     title='Custom World Map with Robots',
#     xaxis=dict(range=[0, 50], autorange=False),
#     yaxis=dict(range=[0, 50], autorange=False),
#     width=800,
#     height=800,
#     showlegend=True
# )

# # Streamlit interface
# st.title("Custom World Map with Robots")
# map_placeholder = st.empty()
# chat_placeholder = st.empty()

# # Simulate robot movement
# while True:
#     for robot_name, robot_data in robot_traces.items():
#         if robot_data['current_index'] < len(robot_data['path']):
#             position = robot_data['path'][robot_data['current_index']]
#             robot_data['trace'].x = [position[0]]
#             robot_data['trace'].y = [position[1]]
            
#             # Update index for next step
#             robot_data['current_index'] += 1
            
#             # Display the updated map
#             with map_placeholder:
#                 st.plotly_chart(fig)
            
#             # Display communication messages
#             if position in robot_data['messages']:
#                 with chat_placeholder:
#                     st.text(robot_data['messages'][position])
#             else:
#                 with chat_placeholder:
#                     st.empty()
    
#     # Wait for a while to simulate real-time movement
#     time.sleep(1)








# import streamlit as st
# import plotly.graph_objects as go
# import time
# import random

# # Define paths and messages for four robots
# robots = {
#     "Explorer Robot": {
#         "path": [(random.randint(0, 10), random.randint(0, 10)), (15, 5), (30, 20), (35, 25)],
#         "color": "red",
#         "messages": {
#             (15, 5): "Explorer Robot reached checkpoint (15, 5).",
#             (30, 20): "Explorer Robot reached checkpoint (30, 20)."
#         }
#     },
#     "Scout Robot": {
#         "path": [(random.randint(0, 10), random.randint(0, 10)), (5, 25), (15, 35), (20, 40)],
#         "color": "green",
#         "messages": {
#             (5, 25): "Scout Robot reached checkpoint (5, 25).",
#             (15, 35): "Scout Robot reached checkpoint (15, 35)."
#         }
#     },
#     "Surveyor Robot": {
#         "path": [(random.randint(0, 10), random.randint(0, 10)), (10, 10), (25, 15), (30, 20)],
#         "color": "blue",
#         "messages": {
#             (10, 10): "Surveyor Robot reached checkpoint (10, 10).",
#             (25, 15): "Surveyor Robot reached checkpoint (25, 15)."
#         }
#     },
#     "Drone Robot": {
#         "path": [(random.randint(0, 10), random.randint(0, 10)), (20, 5), (30, 15), (40, 30)],
#         "color": "orange",
#         "messages": {
#             (20, 5): "Drone Robot reached checkpoint (20, 5).",
#             (30, 15): "Drone Robot reached checkpoint (30, 15)."
#         }
#     }
# }

# # Create a Plotly figure for the map
# fig = go.Figure()

# # Add the grid lines
# for i in range(0, 51, 1):
#     fig.add_trace(go.Scatter(x=[i, i], y=[0, 50], mode='lines', line=dict(color='lightgrey', width=0.5), showlegend=False))
#     fig.add_trace(go.Scatter(x=[0, 50], y=[i, i], mode='lines', line=dict(color='lightgrey', width=0.5), showlegend=False))

# # Add each robot's path and initialize their starting positions
# for robot_name, robot_info in robots.items():
#     path_x, path_y = zip(*robot_info["path"])
#     fig.add_trace(go.Scatter(x=path_x, y=path_y, mode='lines+markers', line=dict(color=robot_info["color"], dash='dash'), marker=dict(size=5), name=f'{robot_name} Path'))
#     robot_trace = go.Scatter(x=[path_x[0]], y=[path_y[0]], mode='markers', marker=dict(symbol='diamond', size=10, color=robot_info["color"]), name=robot_name)
#     fig.add_trace(robot_trace)
#     robots[robot_name]["trace"] = robot_trace

# # Set figure layout
# fig.update_layout(
#     title='Custom World Map with Robots',
#     xaxis=dict(range=[0, 50], autorange=False),
#     yaxis=dict(range=[0, 50], autorange=False),
#     width=600,
#     height=600,
#     showlegend=True
# )

# # Streamlit interface
# st.title("Custom World Map with Robots")
# map_placeholder = st.empty()
# chat_placeholder = st.empty()

# # Simulate robot movement
# for i in range(len(next(iter(robots.values()))["path"])):
#     for robot_name, robot_info in robots.items():
#         if i < len(robot_info["path"]):
#             robot_position = robot_info["path"][i]

#             # Update the robot's position
#             robot_info["trace"].x = [robot_position[0]]
#             robot_info["trace"].y = [robot_position[1]]
            
#             # Display communication messages
#             if robot_position in robot_info["messages"]:
#                 with chat_placeholder:
#                     st.text(robot_info["messages"][robot_position])
#             else:
#                 with chat_placeholder:
#                     st.empty()

#     # Display the updated map
#     with map_placeholder:
#         st.plotly_chart(fig)

#     # Wait for a while to simulate real-time movement
#     time.sleep(1)




# import streamlit as st
# import plotly.graph_objects as go
# import time
# import random

# # Define robots with random start and end points
# robots = {
#     "Explorer Robot": {
#         "color": "blue",
#         "path": [(random.randint(0, 20), random.randint(0, 20)) for _ in range(8)],
#         "messages": {}
#     },
#     "Scout Robot": {
#         "color": "green",
#         "path": [(random.randint(0, 20), random.randint(0, 20)) for _ in range(8)],
#         "messages": {}
#     },
#     "Surveyor Robot": {
#         "color": "purple",
#         "path": [(random.randint(0, 20), random.randint(0, 20)) for _ in range(8)],
#         "messages": {}
#     },
#     "Drone Robot": {
#         "color": "orange",
#         "path": [(random.randint(0, 20), random.randint(0, 20)) for _ in range(8)],
#         "messages": {}
#     }
# }

# # Generate random communication messages
# for robot in robots:
#     checkpoints = random.sample(robots[robot]["path"], k=2)  # 2 random checkpoints
#     robots[robot]["messages"] = {point: f"Alert! {robot} has reached {point} later than expected!" for point in checkpoints}

# # Create a Plotly figure for the map
# fig = go.Figure()

# # Add the grid lines
# for i in range(0, 51, 1):
#     fig.add_trace(go.Scatter(x=[i, i], y=[0, 50], mode='lines', line=dict(color='lightgrey', width=0.5), showlegend=False))
#     fig.add_trace(go.Scatter(x=[0, 50], y=[i, i], mode='lines', line=dict(color='lightgrey', width=0.5), showlegend=False))

# # Add the robots' paths and positions
# robot_traces = {}
# for robot, details in robots.items():
#     path_x, path_y = zip(*details["path"])
#     fig.add_trace(go.Scatter(x=path_x, y=path_y, mode='lines+markers', line=dict(color=details["color"], dash='dash'), marker=dict(size=5), name=f'{robot} Path'))
#     robot_trace = go.Scatter(x=[details["path"][0][0]], y=[details["path"][0][1]], mode='markers', marker=dict(symbol='diamond', size=10, color=details["color"]), name=robot)
#     robot_traces[robot] = robot_trace
#     fig.add_trace(robot_trace)

# # Set figure layout
# fig.update_layout(
#     title='Custom World Map with Robots',
#     xaxis=dict(range=[0, 50], autorange=False),
#     yaxis=dict(range=[0, 50], autorange=False),
#     width=800,
#     height=800,
#     showlegend=True
# )

# # Streamlit interface
# st.title("Custom World Map with Robots")
# map_placeholder = st.empty()
# chat_placeholder = st.empty()

# # Simulate robots' movements
# while True:
#     for robot, details in robots.items():
#         path = details["path"]
#         for position in path:
#             # Update the robot's position
#             robot_traces[robot].x = [position[0]]
#             robot_traces[robot].y = [position[1]]
            
#             # Display the updated map
#             with map_placeholder:
#                 st.plotly_chart(fig)

#             # Display communication messages
#             if position in details["messages"]:
#                 with chat_placeholder:
#                     st.text(details["messages"][position])
#             else:
#                 with chat_placeholder:
#                     st.empty()
            
#             # Wait for a while to simulate real-time movement
#             time.sleep(1)
            
#     # To avoid an infinite loop in the simulation, add a break condition or run in a loop
#     break





# import streamlit as st
# import plotly.graph_objects as go
# import time
# import random

# # # Define robots' paths and messages
# # robots = {
# #     "Explorer Robot": {
# #         "path": [(0, 0), (5, 5), (10, 10), (12, 14), (15, 20)],
# #         "color": "blue",
# #         "messages": {(10, 10): "Alert! Explorer Robot has reached (10, 10) later than expected!",
# #                      (12, 14): "Alert! Explorer Robot has reached (12, 14) later than expected!"}
# #     },
# #     "Scout Robot": {
# #         "path": [(1, 1), (6, 7), (12, 8), (15, 12), (20, 20)],
# #         "color": "green",
# #         "messages": {(6, 7): "Alert! Scout Robot has reached (6, 7) later than expected!",
# #                      (15, 12): "Alert! Scout Robot has reached (15, 12) later than expected!"}
# #     },
# #     "Surveyor Robot": {
# #         "path": [(2, 2), (8, 8), (13, 9), (16, 15), (18, 18)],
# #         "color": "purple",
# #         "messages": {(8, 8): "Alert! Surveyor Robot has reached (8, 8) later than expected!",
# #                      (16, 15): "Alert! Surveyor Robot has reached (16, 15) later than expected!"}
# #     },
# #     "Drone Robot": {
# #         "path": [(0, 10), (5, 15), (10, 12), (13, 16), (20, 20)],
# #         "color": "orange",
# #         "messages": {(5, 15): "Alert! Drone Robot has reached (5, 15) later than expected!",
# #                      (13, 16): "Alert! Drone Robot has reached (13, 16) later than expected!"}
# #     }
# # }

# # Define robots' paths and messages
# robots = {
#     "Explorer Robot": {
#         "path": [(1, 1), (8, 8), (15, 14), (20, 22), (22, 25), (25, 30)],
#         "color": "blue",
#         "messages": {(8, 8): "Alert! Explorer Robot has reached (8, 8) later than expected!",
#                      (15, 14): "Alert! Explorer Robot has reached (15, 14) later than expected!",
#                      (20, 22): "Alert! Explorer Robot has reached (20, 22) later than expected!"}
#     },
#     "Scout Robot": {
#         "path": [(32, 25), (34, 27), (36, 30), (38, 32), (40, 35), (38, 37), (36, 39), (35, 39), (40, 40)],
#         "color": "green",
#         "messages": {(34, 27): "Alert! Scout Robot has reached (34, 27) later than expected!",
#                      (38, 32): "Alert! Scout Robot has reached (38, 32) later than expected!",
#                      (36, 39): "Alert! Scout Robot has reached (36, 39) later than expected!"}
#     },
#     "Surveyor Robot": {
#         "path": [(17, 29), (19, 25), (21, 23), (23, 24), (26, 26), (28, 27), (30, 30)],
#         "color": "purple",
#         "messages": {(19, 25): "Alert! Surveyor Robot has reached (19, 25) later than expected!",
#                      (23, 24): "Alert! Surveyor Robot has reached (23, 24) later than expected!",
#                      (28, 27): "Alert! Surveyor Robot has reached (28, 27) later than expected!"}
#     },
#     "Drone Robot": {
#         "path": [(12, 12), (15, 15), (18, 18), (20, 20), (22, 22), (24, 24), (26, 26), (28, 28), (30, 30), (32, 32), (34, 34), (24, 24)],
#         "color": "red",
#         "messages": {(15, 15): "Alert! Drone Robot has reached (15, 15) later than expected!",
#                      (20, 20): "Alert! Drone Robot has reached (20, 20) later than expected!",
#                      (24, 24): "Alert! Drone Robot has reached (24, 24) later than expected!"}
#     }
# }







# # import random

# # def generate_random_path(start, end, num_points):
# #     """Generate a random path from start to end with a specified number of points."""
# #     path = [start]
# #     for _ in range(num_points - 2):
# #         x = random.uniform(start[0], end[0])
# #         y = random.uniform(start[1], end[1])
# #         path.append((round(x), round(y)))
# #     path.append(end)
# #     return path

# # def generate_messages(path, num_messages):
# #     """Generate random messages for a specified number of points along the path."""
# #     message_points = random.sample(path[1:-1], min(num_messages, len(path) - 2))
# #     messages = {point: f"Alert! Robot has reached {point} later than expected!" for point in message_points}
# #     return messages

# # def generate_robot_paths():
# #     """Generate random paths for the predefined robots."""
# #     robot_details = {
# #         "Explorer Robot": {"color": "blue"},
# #         "Scout Robot": {"color": "green"},
# #         "Surveyor Robot": {"color": "purple"},
# #         "Drone Robot": {"color": "orange"}
# #     }
    
# #     robots = {}
# #     for name, details in robot_details.items():
# #         start = (random.randint(0, 20), random.randint(0, 20))
# #         end = (random.randint(0, 20), random.randint(0, 20))
# #         num_points = random.randint(6, 10)
# #         path = generate_random_path(start, end, num_points)
# #         num_messages = random.randint(1, min(5, num_points - 2))  # Ensure there are enough points for messages
        
# #         robots[name] = {
# #             "path": path,
# #             "color": details["color"],
# #             "messages": generate_messages(path, num_messages)
# #         }
    
# #     return robots

# # # Example usage:
# # robots = generate_robot_paths()
# # # print(robot_paths)





# # import random

# # def generate_random_path(start, end, num_points):
# #     """Generate a random path from start to end with a specified number of points."""
# #     path = [start]
# #     for _ in range(num_points - 2):
# #         x = random.uniform(start[0], end[0])
# #         y = random.uniform(start[1], end[1])
# #         path.append((round(x), round(y)))
# #     path.append(end)
# #     return path

# # def generate_robot_paths():
# #     """Generate random paths for the predefined robots."""
# #     robot_details = {
# #         "Explorer Robot": {"color": "blue"},
# #         "Scout Robot": {"color": "green"},
# #         "Surveyor Robot": {"color": "purple"},
# #         "Drone Robot": {"color": "orange"}
# #     }
    
# #     robots = {}
# #     for name, details in robot_details.items():
# #         start = (random.randint(0, 20), random.randint(0, 20))
# #         end = (random.randint(0, 20), random.randint(0, 20))
# #         num_points = random.randint(6, 10)
# #         path = generate_random_path(start, end, num_points)
        
# #         robots[name] = {
# #             "path": path,
# #             "color": details["color"],
# #             "messages": {}  # Messages can be added later
# #         }
    
# #     return robots

# # # Example usage:
# # robots = generate_robot_paths()
# # # print(robot_paths)




# # Create a Plotly figure for the map
# fig = go.Figure()

# # Add the grid lines
# for i in range(0, 51, 1):
#     fig.add_trace(go.Scatter(x=[i, i], y=[0, 50], mode='lines', line=dict(color='lightgrey', width=0.5), showlegend=False))
#     fig.add_trace(go.Scatter(x=[0, 50], y=[i, i], mode='lines', line=dict(color='lightgrey', width=0.5), showlegend=False))

# # Add the robots' paths and positions
# for robot_name, robot_data in robots.items():
#     path = robot_data["path"]
#     color = robot_data["color"]
#     messages = robot_data["messages"]
    
#     path_x, path_y = zip(*path)
#     fig.add_trace(go.Scatter(x=path_x, y=path_y, mode='lines+markers', line=dict(color=color, dash='dash'), marker=dict(size=5), name=f'{robot_name} Path'))
    
#     # Initialize the robot's starting position
#     robot_position = path[0]
#     robot_trace = go.Scatter(x=[robot_position[0]], y=[robot_position[1]], mode='markers', marker=dict(symbol='diamond', size=10, color=color), name=robot_name)
#     fig.add_trace(robot_trace)

# # Set figure layout
# fig.update_layout(
#     title='Custom World Map with Robots',
#     xaxis=dict(range=[0, 50], autorange=False),
#     yaxis=dict(range=[0, 50], autorange=False),
#     width=800,
#     height=800,
#     showlegend=True
# )

# # Streamlit interface
# st.title("Custom World Map with Robots")
# map_placeholder = st.empty()
# chat_placeholder = st.empty()

# # Simulate robots' movement
# robot_positions = {name: data["path"][0] for name, data in robots.items()}
# while any(pos != path[-1] for name, (path, pos) in zip(robots.keys(), zip([data["path"] for data in robots.values()], robot_positions.values()))):
#     for robot_name, robot_data in robots.items():
#         path = robot_data["path"]
#         color = robot_data["color"]
#         messages = robot_data["messages"]
        
#         current_pos_index = path.index(robot_positions[robot_name])
#         if current_pos_index < len(path) - 1:
#             robot_positions[robot_name] = path[current_pos_index + 1]
#             # Update the robot's position
#             for trace in fig.data:
#                 if trace.name == robot_name:
#                     trace.x = [robot_positions[robot_name][0]]
#                     trace.y = [robot_positions[robot_name][1]]
            
#             # Display the updated map
#             with map_placeholder:
#                 st.plotly_chart(fig)
    
#             # Display communication messages
#             with chat_placeholder:
#                 st.write(f"{robot_name}:")
#                 if robot_positions[robot_name] in messages:
#                     st.text(messages[robot_positions[robot_name]])
#                 else:
#                     st.empty()

#             # Wait for a while to simulate real-time movement
#             time.sleep(1)






# # GOAL WORKS
# import streamlit as st
# import plotly.graph_objects as go
# import time
# import random

# # # Define robots' paths and messages
# # robots = {
# #     "Explorer Robot": {
# #         "path": [(0, 0), (5, 5), (10, 10), (12, 14), (15, 20)],
# #         "color": "blue",
# #         "messages": {(10, 10): "Alert! Explorer Robot has reached (10, 10) later than expected!",
# #                      (12, 14): "Alert! Explorer Robot has reached (12, 14) later than expected!"}
# #     },
# #     "Scout Robot": {
# #         "path": [(1, 1), (6, 7), (12, 8), (15, 12), (20, 20)],
# #         "color": "green",
# #         "messages": {(6, 7): "Alert! Scout Robot has reached (6, 7) later than expected!",
# #                      (15, 12): "Alert! Scout Robot has reached (15, 12) later than expected!"}
# #     },
# #     "Surveyor Robot": {
# #         "path": [(2, 2), (8, 8), (13, 9), (16, 15), (18, 18)],
# #         "color": "purple",
# #         "messages": {(8, 8): "Alert! Surveyor Robot has reached (8, 8) later than expected!",
# #                      (16, 15): "Alert! Surveyor Robot has reached (16, 15) later than expected!"}
# #     },
# #     "Drone Robot": {
# #         "path": [(0, 10), (5, 15), (10, 12), (13, 16), (20, 20)],
# #         "color": "orange",
# #         "messages": {(5, 15): "Alert! Drone Robot has reached (5, 15) later than expected!",
# #                      (13, 16): "Alert! Drone Robot has reached (13, 16) later than expected!"}
# #     }
# # }

# # Define robots' paths and messages
# robots = {
#     "Explorer Robot": {
#         "path": [(1, 1), (8, 8), (15, 14), (20, 22), (22, 25), (25, 30)],
#         "color": "blue",
#         "messages": {(8, 8): "Alert! Explorer Robot has reached (8, 8) later than expected!",
#                      (15, 14): "Alert! Explorer Robot has reached (15, 14) later than expected!",
#                      (20, 22): "Alert! Explorer Robot has reached (20, 22) later than expected!"}
#     },
#     "Scout Robot": {
#         "path": [(32, 25), (34, 27), (36, 30), (38, 32), (40, 35), (38, 37), (36, 39), (35, 39), (40, 40)],
#         "color": "green",
#         "messages": {(34, 27): "Alert! Scout Robot has reached (34, 27) later than expected!",
#                      (38, 32): "Alert! Scout Robot has reached (38, 32) later than expected!",
#                      (36, 39): "Alert! Scout Robot has reached (36, 39) later than expected!"}
#     },
#     "Surveyor Robot": {
#         "path": [(17, 29), (19, 25), (21, 23), (23, 24), (26, 26), (28, 27), (30, 30)],
#         "color": "purple",
#         "messages": {(19, 25): "Alert! Surveyor Robot has reached (19, 25) later than expected!",
#                      (23, 24): "Alert! Surveyor Robot has reached (23, 24) later than expected!",
#                      (28, 27): "Alert! Surveyor Robot has reached (28, 27) later than expected!"}
#     },
#     "Drone Robot": {
#         "path": [(12, 12), (15, 15), (18, 18), (20, 20), (22, 22), (24, 24), (26, 26), (28, 28), (30, 30), (32, 32), (34, 34), (24, 24)],
#         "color": "red",
#         "messages": {(15, 15): "Alert! Drone Robot has reached (15, 15) later than expected!",
#                      (20, 20): "Alert! Drone Robot has reached (20, 20) later than expected!",
#                      (24, 24): "Alert! Drone Robot has reached (24, 24) later than expected!"}
#     }
# }





# # Create a Plotly figure for the map
# fig = go.Figure()

# # Add the grid lines
# for i in range(0, 51, 1):
#     fig.add_trace(go.Scatter(x=[i, i], y=[0, 50], mode='lines', line=dict(color='lightgrey', width=0.5), showlegend=False))
#     fig.add_trace(go.Scatter(x=[0, 50], y=[i, i], mode='lines', line=dict(color='lightgrey', width=0.5), showlegend=False))

# # Add the robots' paths and positions
# for robot_name, robot_data in robots.items():
#     path = robot_data["path"]
#     color = robot_data["color"]
#     messages = robot_data["messages"]
    
#     path_x, path_y = zip(*path)
#     fig.add_trace(go.Scatter(x=path_x, y=path_y, mode='lines+markers', line=dict(color=color, dash='dash'), marker=dict(size=5), name=f'{robot_name} Path'))
    
#     # Initialize the robot's starting position
#     robot_position = path[0]
#     robot_trace = go.Scatter(x=[robot_position[0]], y=[robot_position[1]], mode='markers', marker=dict(symbol='diamond', size=10, color=color), name=robot_name)
#     fig.add_trace(robot_trace)

# # Set figure layout
# fig.update_layout(
#     title='Custom World Map with Robots',
#     xaxis=dict(range=[0, 50], autorange=False),
#     yaxis=dict(range=[0, 50], autorange=False),
#     width=800,
#     height=800,
#     showlegend=True
# )

# # Streamlit interface
# st.title("Custom World Map with Robots")
# map_placeholder = st.empty()
# chat_placeholder = st.empty()

# # Simulate robots' movement
# robot_positions = {name: data["path"][0] for name, data in robots.items()}
# while any(pos != path[-1] for name, (path, pos) in zip(robots.keys(), zip([data["path"] for data in robots.values()], robot_positions.values()))):
#     for robot_name, robot_data in robots.items():
#         path = robot_data["path"]
#         color = robot_data["color"]
#         messages = robot_data["messages"]
        
#         current_pos_index = path.index(robot_positions[robot_name])
#         if current_pos_index < len(path) - 1:
#             robot_positions[robot_name] = path[current_pos_index + 1]
#             # Update the robot's position
#             for trace in fig.data:
#                 if trace.name == robot_name:
#                     trace.x = [robot_positions[robot_name][0]]
#                     trace.y = [robot_positions[robot_name][1]]
            
#             # Display the updated map
#             with map_placeholder:
#                 st.plotly_chart(fig)
    
#             # Display communication messages
#             with chat_placeholder:
#                 st.write(f"{robot_name}:")
#                 if robot_positions[robot_name] in messages:
#                     st.text(messages[robot_positions[robot_name]])
#                 else:
#                     st.empty()

#             # Wait for a while to simulate real-time movement
#             time.sleep(1)








# import streamlit as st
# import plotly.graph_objects as go
# import time
# import numpy as np

# # Define robots' paths and messages
# robots = {
#     "Explorer Robot": {
#         "path": [(1, 1), (2, 3), (3, 5), (4, 7), (5, 9), (6, 11), (7, 13), (8, 15), (9, 17), (10, 19), (11, 21), (12, 23), (13, 25), (14, 27), (15, 29), (16, 30), (17, 31), (18, 32), (19, 33), (20, 34)],
#         "color": "blue",
#         "messages": {(10, 19): "Alert! Explorer Robot has reached (10, 19) later than expected!",
#                      (15, 29): "Alert! Explorer Robot has reached (15, 29) later than expected!",
#                      (20, 34): "Alert! Explorer Robot has reached (20, 34) later than expected!"}
#     },
#     "Scout Robot": {
#         "path": [(2, 5), (3, 7), (4, 9), (5, 11), (6, 13), (7, 15), (8, 17), (9, 19), (10, 21), (11, 23), (12, 25), (13, 27), (14, 29), (15, 31), (16, 33), (17, 35), (18, 37), (19, 39), (20, 40)],
#         "color": "green",
#         "messages": {(10, 21): "Alert! Scout Robot has reached (10, 21) later than expected!",
#                      (15, 31): "Alert! Scout Robot has reached (15, 31) later than expected!",
#                      (20, 40): "Alert! Scout Robot has reached (20, 40) later than expected!"}
#     },
#     "Surveyor Robot": {
#         "path": [(3, 6), (4, 8), (5, 10), (6, 12), (7, 14), (8, 16), (9, 18), (10, 20), (11, 22), (12, 24), (13, 26), (14, 28), (15, 30), (16, 32), (17, 34), (18, 36), (19, 38), (20, 40)],
#         "color": "purple",
#         "messages": {(10, 20): "Alert! Surveyor Robot has reached (10, 20) later than expected!",
#                      (15, 30): "Alert! Surveyor Robot has reached (15, 30) later than expected!",
#                      (20, 40): "Alert! Surveyor Robot has reached (20, 40) later than expected!"}
#     },
#     "Drone Robot": {
#         "path": [(4, 7), (5, 9), (6, 11), (7, 13), (8, 15), (9, 17), (10, 19), (11, 21), (12, 23), (13, 25), (14, 27), (15, 29), (16, 31), (17, 33), (18, 35), (19, 37), (20, 39)],
#         "color": "red",
#         "messages": {(10, 19): "Alert! Drone Robot has reached (10, 19) later than expected!",
#                      (15, 29): "Alert! Drone Robot has reached (15, 29) later than expected!",
#                      (20, 39): "Alert! Drone Robot has reached (20, 39) later than expected!"}
#     }
# }

# # Helper function to find the closest point in the path
# def find_closest_point(current_pos, path):
#     path_np = np.array(path)
#     distances = np.sqrt(np.sum((path_np - np.array(current_pos))**2, axis=1))
#     return path[np.argmin(distances)]

# # Create a Plotly figure for the map
# fig = go.Figure()

# # Add the grid lines
# for i in range(0, 41, 1):  # 40x40 grid for a square map
#     fig.add_trace(go.Scatter(x=[i, i], y=[0, 40], mode='lines', line=dict(color='lightgrey', width=0.5), showlegend=False))
#     fig.add_trace(go.Scatter(x=[0, 40], y=[i, i], mode='lines', line=dict(color='lightgrey', width=0.5), showlegend=False))

# # Add the robots' paths and positions
# for robot_name, robot_data in robots.items():
#     path = robot_data["path"]
#     color = robot_data["color"]
#     messages = robot_data["messages"]
    
#     path_x, path_y = zip(*path)
#     fig.add_trace(go.Scatter(x=path_x, y=path_y, mode='lines+markers', line=dict(color=color, dash='dash'), marker=dict(size=5), name=f'{robot_name} Path'))
    
#     # Initialize the robot's starting position
#     robot_position = path[0]
#     robot_trace = go.Scatter(x=[robot_position[0]], y=[robot_position[1]], mode='markers', marker=dict(symbol='diamond', size=10, color=color), name=robot_name)
#     fig.add_trace(robot_trace)

# # Set figure layout with reduced size for the map
# fig.update_layout(
#     title='Custom World Map with Robots',
#     xaxis=dict(range=[0, 40], autorange=False),
#     yaxis=dict(range=[0, 40], autorange=False),
#     width=800,  # Adjusted width
#     height=600, # Adjusted height
#     showlegend=True
# )

# # Streamlit interface
# st.title("Custom World Map with Robots")

# # Layout: Map above, Chat below
# map_placeholder = st.empty()
# chat_placeholder = st.empty()

# # Simulate robots' movement
# robot_positions = {name: data["path"][0] for name, data in robots.items()}
# while any(pos != path[-1] for name, (path, pos) in zip(robots.keys(), zip([data["path"] for data in robots.values()], robot_positions.values()))):
#     for robot_name, robot_data in robots.items():
#         path = robot_data["path"]
#         color = robot_data["color"]
#         messages = robot_data["messages"]
        
#         current_pos = robot_positions[robot_name]
#         next_pos = find_closest_point(current_pos, path)
        
#         if next_pos != current_pos:
#             # Move robot towards the next position
#             if current_pos[0] < next_pos[0]:
#                 robot_positions[robot_name] = (current_pos[0] + 1, current_pos[1])
#             elif current_pos[0] > next_pos[0]:
#                 robot_positions[robot_name] = (current_pos[0] - 1, current_pos[1])
#             elif current_pos[1] < next_pos[1]:
#                 robot_positions[robot_name] = (current_pos[0], current_pos[1] + 1)
#             elif current_pos[1] > next_pos[1]:
#                 robot_positions[robot_name] = (current_pos[0], current_pos[1] - 1)

#             # Update the robot's position
#             for trace in fig.data:
#                 if trace.name == robot_name:
#                     trace.x = [robot_positions[robot_name][0]]
#                     trace.y = [robot_positions[robot_name][1]]
            
#             # Display the updated map
#             with map_placeholder:
#                 st.plotly_chart(fig)
    
#             # Display communication messages
#             with chat_placeholder:
#                 st.write(f"{robot_name}:")
#                 if robot_positions[robot_name] in messages:
#                     st.text(messages[robot_positions[robot_name]])
#                 else:
#                     st.empty()

#             # Wait for a while to simulate real-time movement
#             time.sleep(0.5)  # Adjust the speed as needed


# # WORKS
# import streamlit as st
# import plotly.graph_objects as go
# import time

# def generate_intermediate_path(start, end):
#     path = [start]
#     x1, y1 = start
#     x2, y2 = end
#     while (x1, y1) != (x2, y2):
#         if x1 < x2:
#             x1 += 1
#         elif x1 > x2:
#             x1 -= 1
#         if y1 < y2:
#             y1 += 1
#         elif y1 > y2:
#             y1 -= 1
#         path.append((x1, y1))
#     return path

# # Define robots' path with intermediate points
# robots = {
#     "Explorer Robot": {
#         "path": [
#             (1, 1), (5, 7), (10, 10), (15, 15), (20, 20)
#         ],
#         "color": "blue",
#         "messages": {
#             (5, 7): "Alert! Explorer Robot has reached (5, 7) later than expected!",
#             (10, 10): "Alert! Explorer Robot has reached (10, 10) later than expected!",
#             (15, 15): "Alert! Explorer Robot has reached (15, 15) later than expected!"
#         }
#     },
#     "Scout Robot": {
#         "path": [
#             (2, 5), (7, 10), (12, 15), (17, 20), (22, 25)
#         ],
#         "color": "green",
#         "messages": {
#             (7, 10): "Alert! Scout Robot has reached (7, 10) later than expected!",
#             (12, 15): "Alert! Scout Robot has reached (12, 15) later than expected!",
#             (17, 20): "Alert! Scout Robot has reached (17, 20) later than expected!"
#         }
#     },
#     "Surveyor Robot": {
#         "path": [
#             (3, 6), (8, 12), (13, 18), (18, 24), (23, 30)
#         ],
#         "color": "purple",
#         "messages": {
#             (8, 12): "Alert! Surveyor Robot has reached (8, 12) later than expected!",
#             (13, 18): "Alert! Surveyor Robot has reached (13, 18) later than expected!",
#             (18, 24): "Alert! Surveyor Robot has reached (18, 24) later than expected!"
#         }
#     },
#     "Drone Robot": {
#         "path": [
#             (4, 7), (9, 14), (14, 21), (19, 28), (24, 35)
#         ],
#         "color": "red",
#         "messages": {
#             (9, 14): "Alert! Drone Robot has reached (9, 14) later than expected!",
#             (14, 21): "Alert! Drone Robot has reached (14, 21) later than expected!",
#             (19, 28): "Alert! Drone Robot has reached (19, 28) later than expected!"
#         }
#     }
# }

# # Generate paths with intermediate points
# for robot_name, robot_data in robots.items():
#     new_path = []
#     path = robot_data["path"]
#     for i in range(len(path) - 1):
#         start = path[i]
#         end = path[i + 1]
#         new_path.extend(generate_intermediate_path(start, end))
#     robots[robot_name]["path"] = new_path

# # Create a Plotly figure for the map
# fig = go.Figure()

# # Add the grid lines
# for i in range(0, 41, 1):  # 40x40 grid for a square map
#     fig.add_trace(go.Scatter(x=[i, i], y=[0, 40], mode='lines', line=dict(color='lightgrey', width=0.5), showlegend=False))
#     fig.add_trace(go.Scatter(x=[0, 40], y=[i, i], mode='lines', line=dict(color='lightgrey', width=0.5), showlegend=False))

# # Add the robots' paths and positions
# for robot_name, robot_data in robots.items():
#     path = robot_data["path"]
#     color = robot_data["color"]
#     messages = robot_data["messages"]
    
#     path_x, path_y = zip(*path)
#     fig.add_trace(go.Scatter(x=path_x, y=path_y, mode='lines+markers', line=dict(color=color, dash='dash'), marker=dict(size=5), name=f'{robot_name} Path'))
    
#     # Initialize the robot's starting position
#     robot_position = path[0]
#     robot_trace = go.Scatter(x=[robot_position[0]], y=[robot_position[1]], mode='markers', marker=dict(symbol='diamond', size=10, color=color), name=robot_name)
#     fig.add_trace(robot_trace)

# # Set figure layout with reduced size for the map
# fig.update_layout(
#     title='Custom World Map with Robots',
#     xaxis=dict(range=[0, 40], autorange=False),
#     yaxis=dict(range=[0, 40], autorange=False),
#     width=800,  # Adjusted width
#     height=600, # Adjusted height
#     showlegend=True
# )

# # Streamlit interface
# st.title("Custom World Map with Robots")

# # Layout: Map above, Chat below
# map_placeholder = st.empty()
# chat_placeholder = st.empty()

# # Simulate robots' movement
# robot_positions = {name: data["path"][0] for name, data in robots.items()}
# while any(pos != path[-1] for name, (path, pos) in zip(robots.keys(), zip([data["path"] for data in robots.values()], robot_positions.values()))):
#     for robot_name, robot_data in robots.items():
#         path = robot_data["path"]
#         color = robot_data["color"]
#         messages = robot_data["messages"]
        
#         current_pos_index = path.index(robot_positions[robot_name])
#         if current_pos_index < len(path) - 1:
#             robot_positions[robot_name] = path[current_pos_index + 1]
#             # Update the robot's position
#             for trace in fig.data:
#                 if trace.name == robot_name:
#                     trace.x = [robot_positions[robot_name][0]]
#                     trace.y = [robot_positions[robot_name][1]]
            
#             # Display the updated map
#             with map_placeholder:
#                 st.plotly_chart(fig)
    
#             # Display communication messages
#             with chat_placeholder:
#                 st.write(f"{robot_name}:")
#                 if robot_positions[robot_name] in messages:
#                     st.text(messages[robot_positions[robot_name]])
#                 else:
#                     st.empty()

#             # Wait for a while to simulate real-time movement
#             time.sleep(1)



# import streamlit as st
# import plotly.graph_objects as go
# import time

# def generate_intermediate_path(start, end):
#     path = [start]
#     x1, y1 = start
#     x2, y2 = end
#     while (x1, y1) != (x2, y2):
#         if x1 < x2:
#             x1 += 1
#         elif x1 > x2:
#             x1 -= 1
#         if y1 < y2:
#             y1 += 1
#         elif y1 > y2:
#             y1 -= 1
#         path.append((x1, y1))
#     return path

# # Define robots' start and end positions
# robot_positions = {
#     "Explorer Robot": {"start": (1, 1), "end": (25, 10)},
#     "Scout Robot": {"start": (14, 15), "end": (20, 35)},
#     "Surveyor Robot": {"start": (30, 26), "end": (33, 20)},
#     "Drone Robot": {"start": (4, 7), "end": (24, 35)}
# }

# # Define colors for robots
# colors = {
#     "Explorer Robot": "blue",
#     "Scout Robot": "green",
#     "Surveyor Robot": "purple",
#     "Drone Robot": "red"
# }

# # Define communication messages for robots
# messages = {
#     "Explorer Robot": {
#         (5, 7): "Alert! Explorer Robot has reached (5, 7) later than expected!",
#         (10, 10): "Alert! Explorer Robot has reached (10, 10) later than expected!",
#         (15, 15): "Alert! Explorer Robot has reached (15, 15) later than expected!"
#     },
#     "Scout Robot": {
#         (7, 10): "Alert! Scout Robot has reached (7, 10) later than expected!",
#         (12, 15): "Alert! Scout Robot has reached (12, 15) later than expected!",
#         (17, 20): "Alert! Scout Robot has reached (17, 20) later than expected!"
#     },
#     "Surveyor Robot": {
#         (8, 12): "Alert! Surveyor Robot has reached (8, 12) later than expected!",
#         (13, 18): "Alert! Surveyor Robot has reached (13, 18) later than expected!",
#         (18, 24): "Alert! Surveyor Robot has reached (18, 24) later than expected!"
#     },
#     "Drone Robot": {
#         (9, 14): "Alert! Drone Robot has reached (9, 14) later than expected!",
#         (14, 21): "Alert! Drone Robot has reached (14, 21) later than expected!",
#         (19, 28): "Alert! Drone Robot has reached (19, 28) later than expected!"
#     }
# }

# # Create robots dictionary with paths and colors
# robots = {}
# for robot_name, pos in robot_positions.items():
#     robots[robot_name] = {
#         "path": generate_intermediate_path(pos["start"], pos["end"]),
#         "color": colors[robot_name],
#         "messages": messages[robot_name]
#     }

# # Create a Plotly figure for the map
# fig = go.Figure()

# # Add the grid lines
# for i in range(0, 41, 1):  # 40x40 grid for a square map
#     fig.add_trace(go.Scatter(x=[i, i], y=[0, 40], mode='lines', line=dict(color='lightgrey', width=0.5), showlegend=False))
#     fig.add_trace(go.Scatter(x=[0, 40], y=[i, i], mode='lines', line=dict(color='lightgrey', width=0.5), showlegend=False))

# # Add the robots' paths and positions
# for robot_name, robot_data in robots.items():
#     path = robot_data["path"]
#     color = robot_data["color"]
#     messages = robot_data["messages"]
    
#     path_x, path_y = zip(*path)
#     fig.add_trace(go.Scatter(x=path_x, y=path_y, mode='lines+markers', line=dict(color=color, dash='dash'), marker=dict(size=5), name=f'{robot_name} Path'))
    
#     # Initialize the robot's starting position
#     robot_position = path[0]
#     robot_trace = go.Scatter(x=[robot_position[0]], y=[robot_position[1]], mode='markers', marker=dict(symbol='diamond', size=10, color=color), name=robot_name)
#     fig.add_trace(robot_trace)

# # Set figure layout with reduced size for the map
# fig.update_layout(
#     title='Custom World Map with Robots',
#     xaxis=dict(range=[0, 40], autorange=False),
#     yaxis=dict(range=[0, 40], autorange=False),
#     width=800,  # Adjusted width
#     height=600, # Adjusted height
#     showlegend=True
# )

# # Layout: Map above, Chat below
# map_placeholder = st.empty()
# chat_placeholder = st.empty()

# # Simulate robots' movement
# robot_positions_current = {name: data["path"][0] for name, data in robots.items()}
# while any(pos != path[-1] for name, (path, pos) in zip(robots.keys(), zip([data["path"] for data in robots.values()], robot_positions_current.values()))):
#     for robot_name, robot_data in robots.items():
#         path = robot_data["path"]
#         color = robot_data["color"]
#         messages = robot_data["messages"]
        
#         current_pos_index = path.index(robot_positions_current[robot_name])
#         if current_pos_index < len(path) - 1:
#             robot_positions_current[robot_name] = path[current_pos_index + 1]
#             # Update the robot's position
#             for trace in fig.data:
#                 if trace.name == robot_name:
#                     trace.x = [robot_positions_current[robot_name][0]]
#                     trace.y = [robot_positions_current[robot_name][1]]
            
#             # Display the updated map
#             with map_placeholder:
#                 st.plotly_chart(fig)
    
#             # Display communication messages
#             with chat_placeholder:
#                 st.write(f"{robot_name}:")
#                 if robot_positions_current[robot_name] in messages:
#                     st.text(messages[robot_positions_current[robot_name]])
#                 else:
#                     st.empty()

#             # Wait for a while to simulate real-time movement
#             time.sleep(0.3)









# import streamlit as st
# import plotly.graph_objects as go
# import time

# def generate_intermediate_path(start, end):
#     path = [start]
#     x1, y1 = start
#     x2, y2 = end
#     while (x1, y1) != (x2, y2):
#         if x1 < x2:
#             x1 += 1
#         elif x1 > x2:
#             x1 -= 1
#         if y1 < y2:
#             y1 += 1
#         elif y1 > y2:
#             y1 -= 1
#         path.append((x1, y1))
#     return path

# def generate_messages(path):
#     messages = {}
#     num_points = len(path)
#     intervals = max(1, num_points // 4)  # Messages at every quarter of the path
#     for i in range(1, num_points):
#         if i % intervals == 0:
#             messages[path[i]] = f"Alert! Robot has reached {path[i]}."
#     if path[-1] not in messages:
#         messages[path[-1]] = f"Robot has reached its destination at {path[-1]}."
#     return messages

# # Define robots' start and end positions
# robot_positions = {
#     "Explorer Robot": {"start": (1, 1), "end": (25, 10)},
#     "Scout Robot": {"start": (14, 15), "end": (20, 35)},
#     "Surveyor Robot": {"start": (30, 26), "end": (33, 20)},
#     "Drone Robot": {"start": (4, 7), "end": (24, 35)}
# }


# # Define colors for robots
# colors = {
#     "Explorer Robot": "blue",
#     "Scout Robot": "green",
#     "Surveyor Robot": "purple",
#     "Drone Robot": "red"
# }

# # Create robots dictionary with paths, colors, and messages
# robots = {}
# for robot_name, pos in robot_positions.items():
#     path = generate_intermediate_path(pos["start"], pos["end"])
#     robots[robot_name] = {
#         "path": path,
#         "color": colors[robot_name],
#         "messages": generate_messages(path)
#     }

# # Create a Plotly figure for the map
# fig = go.Figure()

# # Add the grid lines
# for i in range(0, 41, 1):  # 40x40 grid for a square map
#     fig.add_trace(go.Scatter(x=[i, i], y=[0, 40], mode='lines', line=dict(color='lightgrey', width=0.5), showlegend=False))
#     fig.add_trace(go.Scatter(x=[0, 40], y=[i, i], mode='lines', line=dict(color='lightgrey', width=0.5), showlegend=False))

# # Add the robots' paths and positions
# for robot_name, robot_data in robots.items():
#     path = robot_data["path"]
#     color = robot_data["color"]
#     messages = robot_data["messages"]
    
#     path_x, path_y = zip(*path)
#     fig.add_trace(go.Scatter(x=path_x, y=path_y, mode='lines+markers', line=dict(color=color, dash='dash'), marker=dict(size=5), name=f'{robot_name} Path'))
    
#     # Initialize the robot's starting position
#     robot_position = path[0]
#     robot_trace = go.Scatter(x=[robot_position[0]], y=[robot_position[1]], mode='markers', marker=dict(symbol='diamond', size=10, color=color), name=robot_name)
#     fig.add_trace(robot_trace)

# # Set figure layout with reduced size for the map
# fig.update_layout(
#     title='Custom World Map with Robots',
#     xaxis=dict(range=[0, 40], autorange=False),
#     yaxis=dict(range=[0, 40], autorange=False),
#     width=800,  # Adjusted width
#     height=600, # Adjusted height
#     showlegend=True
# )

# # Layout: Map above, Chat below
# map_placeholder = st.empty()
# chat_placeholder = st.empty()

# # Simulate robots' movement
# robot_positions_current = {name: data["path"][0] for name, data in robots.items()}
# while any(pos != path[-1] for name, (path, pos) in zip(robots.keys(), zip([data["path"] for data in robots.values()], robot_positions_current.values()))):
#     for robot_name, robot_data in robots.items():
#         path = robot_data["path"]
#         color = robot_data["color"]
#         messages = robot_data["messages"]
        
#         current_pos_index = path.index(robot_positions_current[robot_name])
#         if current_pos_index < len(path) - 1:
#             robot_positions_current[robot_name] = path[current_pos_index + 1]
#             # Update the robot's position
#             for trace in fig.data:
#                 if trace.name == robot_name:
#                     trace.x = [robot_positions_current[robot_name][0]]
#                     trace.y = [robot_positions_current[robot_name][1]]
            
#             # Display the updated map
#             with map_placeholder:
#                 st.plotly_chart(fig)
    
#             # Display communication messages
#             with chat_placeholder:
#                 st.write(f"{robot_name}:")
#                 if robot_positions_current[robot_name] in messages:
#                     st.text(messages[robot_positions_current[robot_name]])
#                 else:
#                     st.empty()

#             # Wait for a while to simulate real-time movement
#             time.sleep(1)


# # Final revert
# import streamlit as st
# import plotly.graph_objects as go
# import time

# def generate_intermediate_path(start, end):
#     path = [start]
#     x1, y1 = start
#     x2, y2 = end
#     while (x1, y1) != (x2, y2):
#         if x1 < x2:
#             x1 += 1
#         elif x1 > x2:
#             x1 -= 1
#         if y1 < y2:
#             y1 += 1
#         elif y1 > y2:
#             y1 -= 1
#         path.append((x1, y1))
#     return path

# def generate_messages(path, robot_name):
#     messages = {}
#     num_points = len(path)
#     # intervals = max(1, num_points // 4)  # Messages at every quarter of the path
#     intervals = max(1, num_points // 6)  # Messages at every quarter of the path
#     for i in range(1, num_points):
#         if i % intervals == 0:
#             messages[path[i]] = f"Alert! {robot_name} is delayed and has reached {path[i]}."
#     if path[-1] not in messages:
#         messages[path[-1]] = f"{robot_name} has reached its destination at {path[-1]}."
#     return messages

# # Define robots' start and end positions
# robot_positions = {
#     "Explorer Robot": {"start": (1, 1), "end": (25, 10)},
#     "Scout Robot": {"start": (14, 15), "end": (48, 35)},
#     "Surveyor Robot": {"start": (30, 26), "end": (47, 48)},
#     "Drone Robot": {"start": (4, 7), "end": (24, 35)}
# }

# # Define colors for robots
# colors = {
#     "Explorer Robot": "blue",
#     "Scout Robot": "green",
#     "Surveyor Robot": "purple",
#     "Drone Robot": "red"
# }

# # Create robots dictionary with paths, colors, and messages
# robots = {}
# for robot_name, pos in robot_positions.items():
#     path = generate_intermediate_path(pos["start"], pos["end"])
#     robots[robot_name] = {
#         "path": path,
#         "color": colors[robot_name],
#         "messages": generate_messages(path, robot_name)
#     }

# # Create a Plotly figure for the map
# fig = go.Figure()

# # Add the grid lines for a 50x50 map
# for i in range(0, 51, 1):  # 50x50 grid
#     fig.add_trace(go.Scatter(x=[i, i], y=[0, 50], mode='lines', line=dict(color='lightgrey', width=0.5), showlegend=False))
#     fig.add_trace(go.Scatter(x=[0, 50], y=[i, i], mode='lines', line=dict(color='lightgrey', width=0.5), showlegend=False))

# # Add the robots' paths and positions
# for robot_name, robot_data in robots.items():
#     path = robot_data["path"]
#     color = robot_data["color"]
#     messages = robot_data["messages"]
    
#     path_x, path_y = zip(*path)
#     fig.add_trace(go.Scatter(x=path_x, y=path_y, mode='lines+markers', line=dict(color=color, dash='dash'), marker=dict(size=5), name=f'{robot_name} Path'))
    
#     # Initialize the robot's starting position
#     robot_position = path[0]
#     robot_trace = go.Scatter(x=[robot_position[0]], y=[robot_position[1]], mode='markers', marker=dict(symbol='diamond', size=10, color=color), name=robot_name)
#     fig.add_trace(robot_trace)

# # Set figure layout with reduced size for the map
# fig.update_layout(
#     title='Custom World Map with Robots',
#     xaxis=dict(range=[0, 50], autorange=False),
#     yaxis=dict(range=[0, 50], autorange=False),
#     width=1000,  # Adjusted width for 50x50 grid
#     height=800,  # Adjusted height for 50x50 grid
#     showlegend=True
# )

# fig.add_trace(go.Scatter(x=[i, i], y=[0, 50], mode='lines', line=dict(color='lightgrey', width=1), showlegend=False))
# fig.add_trace(go.Scatter(x=[0, 50], y=[i, i], mode='lines', line=dict(color='lightgrey', width=1), showlegend=False))
# fig.update_layout(
#     paper_bgcolor='lightgrey',
#     plot_bgcolor='white'
# )

# # fig.add_trace(go.Scatter(
# #     x=[robot_position[0]], 
# #     y=[robot_position[1]], 
# #     mode='markers', 
# #     marker=dict(
# #         size=15, 
# #         color=color, 
# #         symbol='circle', 
# #         line=dict(width=2, color='black')
# #     ), 
# #     name=robot_name
# # ))
# # fig.add_trace(go.Scatter(
# #     x=[robot_position[0]], 
# #     y=[robot_position[1]], 
# #     mode='markers+text', 
# #     text=[robot_name], 
# #     textposition='top center',
# #     marker=dict(
# #         size=15, 
# #         color=color
# #     )
# # ))
# # fig.add_trace(go.Scatter(
# #     x=path_x, 
# #     y=path_y, 
# #     mode='lines+markers', 
# #     line=dict(color=color, dash='dot'), 
# #     marker=dict(size=5), 
# #     name=f'{robot_name} Path'
# # ))

# fig.update_layout(
#     title='Robots Navigation Map',
#     xaxis_title='X Coordinate',
#     yaxis_title='Y Coordinate',
#     legend_title='Robots'
# )
# st.sidebar.header('Simulation Controls')
# start_button = st.sidebar.button('Start Simulation')


# # Layout: Map above, Chat below
# map_placeholder = st.empty()
# chat_placeholder = st.empty()




# # Simulate robots' movement
# robot_positions_current = {name: data["path"][0] for name, data in robots.items()}
# while any(pos != path[-1] for name, (path, pos) in zip(robots.keys(), zip([data["path"] for data in robots.values()], robot_positions_current.values()))):
#     for robot_name, robot_data in robots.items():
#         path = robot_data["path"]
#         color = robot_data["color"]
#         messages = robot_data["messages"]
        
#         current_pos_index = path.index(robot_positions_current[robot_name])
#         if current_pos_index < len(path) - 1:
#             robot_positions_current[robot_name] = path[current_pos_index + 1]
#             # Update the robot's position
#             for trace in fig.data:
#                 if trace.name == robot_name:
#                     trace.x = [robot_positions_current[robot_name][0]]
#                     trace.y = [robot_positions_current[robot_name][1]]
            
#             # Display the updated map
#             with map_placeholder:
#                 st.plotly_chart(fig)
    
#             # Display communication messages
#             with chat_placeholder:
#                 st.write(f"{robot_name}:")
#                 if robot_positions_current[robot_name] in messages:
#                     st.text(messages[robot_positions_current[robot_name]])
#                 else:
#                     st.empty()

#             # Wait for a while to simulate real-time movement
#             time.sleep(1)



# import streamlit as st
# import plotly.graph_objects as go
# import time

# def generate_intermediate_path(start, end):
#     path = [start]
#     x1, y1 = start
#     x2, y2 = end
#     while (x1, y1) != (x2, y2):
#         if x1 < x2:
#             x1 += 1
#         elif x1 > x2:
#             x1 -= 1
#         if y1 < y2:
#             y1 += 1
#         elif y1 > y2:
#             y1 -= 1
#         path.append((x1, y1))
#     return path

# def generate_messages(path, robot_name):
#     messages = {}
#     num_points = len(path)
#     intervals = max(1, num_points // 6)  # Messages at every quarter of the path
#     for i in range(1, num_points):
#         if i % intervals == 0:
#             messages[path[i]] = f"Alert! {robot_name} is delayed and has reached {path[i]}."
#     if path[-1] not in messages:
#         messages[path[-1]] = f"{robot_name} has reached its destination at {path[-1]}."
#     return messages

# # Define robots' start and end positions
# robot_positions = {
#     "Explorer Robot": {"start": (1, 1), "end": (25, 10)},
#     "Scout Robot": {"start": (14, 15), "end": (48, 35)},
#     "Surveyor Robot": {"start": (30, 26), "end": (47, 48)},
#     "Drone Robot": {"start": (4, 7), "end": (24, 35)}
# }

# # Define colors for robots
# colors = {
#     "Explorer Robot": "blue",
#     "Scout Robot": "green",
#     "Surveyor Robot": "purple",
#     "Drone Robot": "red"
# }

# # Create robots dictionary with paths, colors, and messages
# robots = {}
# for robot_name, pos in robot_positions.items():
#     path = generate_intermediate_path(pos["start"], pos["end"])
#     robots[robot_name] = {
#         "path": path,
#         "color": colors[robot_name],
#         "messages": generate_messages(path, robot_name)
#     }

# # Create a Plotly figure for the map
# fig = go.Figure()

# # Add the grid lines for a 50x50 map with improved appearance
# for i in range(0, 51, 1):
#     fig.add_trace(go.Scatter(x=[i, i], y=[0, 50], mode='lines', line=dict(color='lightgrey', width=1), showlegend=False))
#     fig.add_trace(go.Scatter(x=[0, 50], y=[i, i], mode='lines', line=dict(color='lightgrey', width=1), showlegend=False))

# # Add the robots' paths and positions with enhanced styling
# for robot_name, robot_data in robots.items():
#     path = robot_data["path"]
#     color = robot_data["color"]
#     messages = robot_data["messages"]
    
#     path_x, path_y = zip(*path)
#     fig.add_trace(go.Scatter(x=path_x, y=path_y, mode='lines+markers', line=dict(color=color, dash='dot'), marker=dict(size=6), name=f'{robot_name} Path'))
    
#     robot_position = path[0]
#     fig.add_trace(go.Scatter(
#         x=[robot_position[0]], 
#         y=[robot_position[1]], 
#         mode='markers+text', 
#         marker=dict(size=15, color=color, symbol='circle', line=dict(width=2, color='black')), 
#         text=[robot_name], 
#         textposition='top center', 
#         name=robot_name
#     ))

# fig.update_layout(
#     title='Enhanced Robots Navigation Map',
#     xaxis=dict(range=[0, 50], autorange=False, title='X Coordinate'),
#     yaxis=dict(range=[0, 50], autorange=False, title='Y Coordinate'),
#     width=1200,
#     height=900,
#     paper_bgcolor='lightgrey',
#     plot_bgcolor='white',
#     showlegend=True
# )

# # Layout: Map above, Chat below
# map_placeholder = st.empty()
# chat_placeholder = st.empty()

# # Simulate robots' movement
# robot_positions_current = {name: data["path"][0] for name, data in robots.items()}
# while any(pos != path[-1] for name, (path, pos) in zip(robots.keys(), zip([data["path"] for data in robots.values()], robot_positions_current.values()))):
#     for robot_name, robot_data in robots.items():
#         path = robot_data["path"]
#         color = robot_data["color"]
#         messages = robot_data["messages"]
        
#         current_pos_index = path.index(robot_positions_current[robot_name])
#         if current_pos_index < len(path) - 1:
#             robot_positions_current[robot_name] = path[current_pos_index + 1]
#             # Update the robot's position
#             for trace in fig.data:
#                 if trace.name == robot_name:
#                     trace.x = [robot_positions_current[robot_name][0]]
#                     trace.y = [robot_positions_current[robot_name][1]]
            
#             # Display the updated map
#             with map_placeholder:
#                 st.plotly_chart(fig)
    
#             # Display communication messages
#             with chat_placeholder:
#                 st.markdown(f"**{robot_name}:**")
#                 if robot_positions_current[robot_name] in messages:
#                     st.text(messages[robot_positions_current[robot_name]])
#                 else:
#                     st.empty()

#             # Wait for a while to simulate real-time movement
#             time.sleep(1)






# import streamlit as st
# import plotly.graph_objects as go
# import time
# import random

# def generate_intermediate_path(start, end):
#     path = [start]
#     x1, y1 = start
#     x2, y2 = end
#     while (x1, y1) != (x2, y2):
#         if x1 < x2:
#             x1 += 1
#         elif x1 > x2:
#             x1 -= 1
#         if y1 < y2:
#             y1 += 1
#         elif y1 > y2:
#             y1 -= 1
#         path.append((x1, y1))
#     return path

# def generate_messages(path, robot_name):
#     messages = {}
#     num_points = len(path)
#     intervals = max(1, num_points // 6)  # Messages at every sixth of the path
#     for i in range(1, num_points):
#         if i % intervals == 0:
#             messages[path[i]] = f"Alert! {robot_name} is delayed and has reached {path[i]}."
#     if path[-1] not in messages:
#         messages[path[-1]] = f"{robot_name} has reached its destination at {path[-1]}."
#     return messages

# def generate_obstacles(num_obstacles, robot_paths):
#     obstacles = []
#     for _ in range(num_obstacles):
#         x = random.randint(0, 50)
#         y = random.randint(0, 50)
#         if any((x, y) in path for path in robot_paths):
#             continue  # Skip if obstacle is on a robot's path
#         obstacles.append((x, y))
#     return obstacles

# # Define robots' start and end positions
# robot_positions = {
#     "Explorer Robot": {"start": (1, 1), "end": (25, 10)},
#     "Scout Robot": {"start": (14, 15), "end": (48, 35)},
#     "Surveyor Robot": {"start": (30, 26), "end": (47, 48)},
#     "Drone Robot": {"start": (4, 7), "end": (24, 35)}
# }

# # Define colors for robots
# colors = {
#     "Explorer Robot": "blue",
#     "Scout Robot": "green",
#     "Surveyor Robot": "purple",
#     "Drone Robot": "red"
# }

# # Create robots dictionary with paths, colors, and messages
# robots = {}
# all_paths = []
# for robot_name, pos in robot_positions.items():
#     path = generate_intermediate_path(pos["start"], pos["end"])
#     all_paths.append(path)
#     robots[robot_name] = {
#         "path": path,
#         "color": colors[robot_name],
#         "messages": generate_messages(path, robot_name)
#     }

# # Generate obstacles
# num_obstacles = 50
# obstacles = generate_obstacles(num_obstacles, all_paths)

# # Create a Plotly figure for the map
# fig = go.Figure()

# # Add obstacles to the map in a single trace
# obstacle_x, obstacle_y = zip(*obstacles) if obstacles else ([], [])
# fig.add_trace(go.Scatter(
#     x=obstacle_x, 
#     y=obstacle_y, 
#     mode='markers', 
#     marker=dict(size=10, color='brown', symbol='cross'), 
#     name='Obstacle'
# ))

# # Add the robots' paths and positions with enhanced styling
# for robot_name, robot_data in robots.items():
#     path = robot_data["path"]
#     color = robot_data["color"]
#     messages = robot_data["messages"]
    
#     path_x, path_y = zip(*path)
#     fig.add_trace(go.Scatter(x=path_x, y=path_y, mode='lines+markers', line=dict(color=color, dash='dot'), marker=dict(size=6), name=f'{robot_name} Path'))
    
#     robot_position = path[0]
#     fig.add_trace(go.Scatter(
#         x=[robot_position[0]], 
#         y=[robot_position[1]], 
#         mode='markers+text', 
#         marker=dict(size=15, color=color, symbol='circle', line=dict(width=2, color='black')), 
#         text=[robot_name], 
#         textposition='top center', 
#         name=robot_name
#     ))

# fig.update_layout(
#     title='Enhanced Robots Navigation Map with Obstacles',
#     xaxis=dict(range=[0, 50], autorange=False, title='X Coordinate'),
#     yaxis=dict(range=[0, 50], autorange=False, title='Y Coordinate'),
#     width=1200,
#     height=900,
#     paper_bgcolor='lightgrey',  # Changed to light grey
#     plot_bgcolor='white',
#     showlegend=True
# )

# # Layout: Map above, Chat below
# map_placeholder = st.empty()
# chat_placeholder = st.empty()

# # Simulate robots' movement
# robot_positions_current = {name: data["path"][0] for name, data in robots.items()}
# while any(pos != path[-1] for name, (path, pos) in zip(robots.keys(), zip([data["path"] for data in robots.values()], robot_positions_current.values()))):
#     for robot_name, robot_data in robots.items():
#         path = robot_data["path"]
#         color = robot_data["color"]
#         messages = robot_data["messages"]
        
#         current_pos_index = path.index(robot_positions_current[robot_name])
#         if current_pos_index < len(path) - 1:
#             robot_positions_current[robot_name] = path[current_pos_index + 1]
#             # Update the robot's position
#             for trace in fig.data:
#                 if trace.name == robot_name:
#                     trace.x = [robot_positions_current[robot_name][0]]
#                     trace.y = [robot_positions_current[robot_name][1]]
            
#             # Display the updated map
#             with map_placeholder:
#                 st.plotly_chart(fig)
    
#             # Display communication messages
#             with chat_placeholder:
#                 st.markdown(f"**{robot_name}:**")
#                 if robot_positions_current[robot_name] in messages:
#                     st.text(messages[robot_positions_current[robot_name]])
#                 else:
#                     st.empty()

#             # Wait for a while to simulate real-time movement
#             time.sleep(1)



# # End v1
# import streamlit as st
# import plotly.graph_objects as go
# import time
# import random

# def generate_intermediate_path(start, end):
#     path = [start]
#     x1, y1 = start
#     x2, y2 = end
#     while (x1, y1) != (x2, y2):
#         if x1 < x2:
#             x1 += 1
#         elif x1 > x2:
#             x1 -= 1
#         if y1 < y2:
#             y1 += 1
#         elif y1 > y2:
#             y1 -= 1
#         path.append((x1, y1))
#     return path

# def generate_messages(path, robot_name, color):
#     messages = {}
#     num_points = len(path)
#     intervals = max(1, num_points // 6)  # Messages at every sixth of the path
#     for i in range(1, num_points):
#         if i % intervals == 0:
#             messages[path[i]] = f"<b>Alert! <span style='color:{color};'>{robot_name}</span> is delayed and has reached {path[i]}.</b>"
#     if path[-1] not in messages:
#         messages[path[-1]] = f"<b><span style='color:{color};'>{robot_name}</span> has reached its destination at {path[-1]}.</b>"
#     return messages

# def generate_obstacles(num_obstacles, robot_paths):
#     obstacles = []
#     for _ in range(num_obstacles):
#         x = random.randint(0, 50)
#         y = random.randint(0, 50)
#         if any((x, y) in path for path in robot_paths):
#             continue  # Skip if obstacle is on a robot's path
#         obstacles.append((x, y))
#     return obstacles

# # Define robots' start and end positions
# robot_positions = {
#     "Explorer Robot": {"start": (1, 1), "end": (25, 10)},
#     "Scout Robot": {"start": (14, 15), "end": (48, 35)},
#     "Surveyor Robot": {"start": (30, 26), "end": (47, 48)},
#     "Drone Robot": {"start": (4, 7), "end": (24, 35)}
# }

# # Define colors for robots
# colors = {
#     "Explorer Robot": "blue",
#     "Scout Robot": "green",
#     "Surveyor Robot": "purple",
#     "Drone Robot": "red"
# }

# # Create robots dictionary with paths, colors, and messages
# robots = {}
# all_paths = []
# for robot_name, pos in robot_positions.items():
#     path = generate_intermediate_path(pos["start"], pos["end"])
#     all_paths.append(path)
#     robots[robot_name] = {
#         "path": path,
#         "color": colors[robot_name],
#         "messages": generate_messages(path, robot_name, colors[robot_name])
#     }

# # Generate obstacles
# num_obstacles = 50
# obstacles = generate_obstacles(num_obstacles, all_paths)

# # Create a Plotly figure for the map
# fig = go.Figure()



# # Add obstacles to the map in a single trace
# obstacle_x, obstacle_y = zip(*obstacles) if obstacles else ([], [])
# fig.add_trace(go.Scatter(
#     x=obstacle_x, 
#     y=obstacle_y, 
#     mode='markers', 
#     marker=dict(size=10, color='brown', symbol='cross'), 
#     name='Obstacle'
# ))

# # Add the robots' paths and positions with enhanced styling
# for robot_name, robot_data in robots.items():
#     path = robot_data["path"]
#     color = robot_data["color"]
#     messages = robot_data["messages"]
    
#     path_x, path_y = zip(*path)
#     fig.add_trace(go.Scatter(x=path_x, y=path_y, mode='lines+markers', line=dict(color=color, dash='dot'), marker=dict(size=6), name=f'{robot_name} Path'))
    
#     robot_position = path[0]
#     fig.add_trace(go.Scatter(
#         x=[robot_position[0]], 
#         y=[robot_position[1]], 
#         mode='markers+text', 
#         marker=dict(size=15, color=color, symbol='circle', line=dict(width=2, color='black')), 
#         text=[robot_name], 
#         textposition='top center', 
#         name=robot_name
#     ))

# fig.update_layout(
#     title='Enhanced Robots Navigation Map with Obstacles',
#     xaxis=dict(range=[0, 50], autorange=False, title='X Coordinate'),
#     yaxis=dict(range=[0, 50], autorange=False, title='Y Coordinate'),
#     width=1200,
#     height=900,
#     paper_bgcolor='lightgrey',  # Changed to light grey
#     plot_bgcolor='white',
#     showlegend=True
# )

# # Layout: Map above, Chat below
# map_placeholder = st.empty()
# chat_placeholder = st.empty()

# # Simulate robots' movement
# robot_positions_current = {name: data["path"][0] for name, data in robots.items()}
# while any(pos != path[-1] for name, (path, pos) in zip(robots.keys(), zip([data["path"] for data in robots.values()], robot_positions_current.values()))):
#     for robot_name, robot_data in robots.items():
#         path = robot_data["path"]
#         color = robot_data["color"]
#         messages = robot_data["messages"]
        
#         current_pos_index = path.index(robot_positions_current[robot_name])
#         if current_pos_index < len(path) - 1:
#             robot_positions_current[robot_name] = path[current_pos_index + 1]
#             # Update the robot's position
#             for trace in fig.data:
#                 if trace.name == robot_name:
#                     trace.x = [robot_positions_current[robot_name][0]]
#                     trace.y = [robot_positions_current[robot_name][1]]
            
#             # Display the updated map
#             with map_placeholder:
#                 st.plotly_chart(fig)
    
#             # Display communication messages
#             with chat_placeholder:
#                 st.markdown(f"**{robot_name}:**")
#                 if robot_positions_current[robot_name] in messages:
#                     st.markdown(messages[robot_positions_current[robot_name]], unsafe_allow_html=True)
#                 else:
#                     st.empty()

#             # Wait for a while to simulate real-time movement
#             time.sleep(1)




# # # END V2
# import streamlit as st
# import plotly.graph_objects as go
# import time
# import random

# def generate_intermediate_path(start, end):
#     path = [start]
#     x1, y1 = start
#     x2, y2 = end
#     while (x1, y1) != (x2, y2):
#         if x1 < x2:
#             x1 += 1
#         elif x1 > x2:
#             x1 -= 1
#         if y1 < y2:
#             y1 += 1
#         elif y1 > y2:
#             y1 -= 1
#         path.append((x1, y1))
#     return path

# def generate_messages(path, robot_name, color):
#     messages = {}
#     num_points = len(path)
#     intervals = max(1, num_points // 6)  # Messages at every sixth of the path
#     for i in range(1, num_points):
#         if i % intervals == 0:
#             messages[path[i]] = f"<b>Alert! <span style='color:{color};'>{robot_name}</span> is delayed and has reached {path[i]}.</b>"
#     if path[-1] not in messages:
#         messages[path[-1]] = f"<b><span style='color:{color};'>{robot_name}</span> has reached its destination at {path[-1]}.</b>"
#     return messages

# def generate_obstacles(num_obstacles, robot_paths):
#     obstacles = []
#     for _ in range(num_obstacles):
#         x = random.randint(0, 50)
#         y = random.randint(0, 50)
#         if any((x, y) in path for path in robot_paths):
#             continue  # Skip if obstacle is on a robot's path
#         obstacles.append((x, y))
#     return obstacles

# # Define robots' start and end positions
# robot_positions = {
#     "Explorer Robot": {"start": (1, 1), "end": (25, 10)},
#     "Scout Robot": {"start": (14, 15), "end": (48, 35)},
#     "Surveyor Robot": {"start": (30, 26), "end": (47, 48)},
#     "Drone Robot": {"start": (4, 7), "end": (24, 35)}
# }

# # Define colors for robots
# colors = {
#     "Explorer Robot": "blue",
#     "Scout Robot": "green",
#     "Surveyor Robot": "purple",
#     "Drone Robot": "red"
# }

# # Create robots dictionary with paths, colors, and messages
# robots = {}
# all_paths = []
# for robot_name, pos in robot_positions.items():
#     path = generate_intermediate_path(pos["start"], pos["end"])
#     all_paths.append(path)
#     robots[robot_name] = {
#         "path": path,
#         "color": colors[robot_name],
#         "messages": generate_messages(path, robot_name, colors[robot_name])
#     }

# # Generate obstacles
# num_obstacles = 50
# obstacles = generate_obstacles(num_obstacles, all_paths)

# # Create a Plotly figure for the map
# fig = go.Figure()

# # Add obstacles to the map in a single trace
# obstacle_x, obstacle_y = zip(*obstacles) if obstacles else ([], [])
# fig.add_trace(go.Scatter(
#     x=obstacle_x, 
#     y=obstacle_y, 
#     mode='markers', 
#     marker=dict(size=10, color='brown', symbol='cross'), 
#     name='Obstacle'
# ))

# # Add the robots' paths and positions with enhanced styling
# for robot_name, robot_data in robots.items():
#     path = robot_data["path"]
#     color = robot_data["color"]
#     messages = robot_data["messages"]
    
#     fig.add_trace(go.Scatter(x=[], y=[], mode='lines+markers', line=dict(color=color, dash='dot'), marker=dict(size=6), name=f'{robot_name} Path'))
    
#     robot_position = path[0]
#     fig.add_trace(go.Scatter(
#         x=[robot_position[0]], 
#         y=[robot_position[1]], 
#         mode='markers+text', 
#         marker=dict(size=15, color=color, symbol='circle', line=dict(width=2, color='black')), 
#         text=[robot_name], 
#         textposition='top center', 
#         name=robot_name
#     ))

# fig.update_layout(
#     title='Enhanced Robots Navigation Map with Obstacles',
#     xaxis=dict(range=[0, 50], autorange=False, title='X Coordinate'),
#     yaxis=dict(range=[0, 50], autorange=False, title='Y Coordinate'),
#     width=1200,
#     height=900,
#     paper_bgcolor='lightgrey',  # Changed to light grey
#     plot_bgcolor='white',
#     showlegend=True
# )

# # Layout: Map above, Chat below
# map_placeholder = st.empty()
# chat_placeholder = st.empty()

# # Simulate robots' movement
# robot_positions_current = {name: data["path"][0] for name, data in robots.items()}
# while any(pos != path[-1] for name, (path, pos) in zip(robots.keys(), zip([data["path"] for data in robots.values()], robot_positions_current.values()))):
#     for robot_name, robot_data in robots.items():
#         path = robot_data["path"]
#         color = robot_data["color"]
#         messages = robot_data["messages"]
        
#         current_pos_index = path.index(robot_positions_current[robot_name])
#         if current_pos_index < len(path) - 1:
#             robot_positions_current[robot_name] = path[current_pos_index + 1]
            
#             # Update the visible part of the path
#             start_index = max(0, current_pos_index - 2)
#             end_index = min(len(path), current_pos_index + 3)
#             visible_path = path[start_index:end_index]
#             path_x, path_y = zip(*visible_path)

#             # Set opacities for fading effect
#             opacities = [0.2, 0.5, 1.0, 0.5, 0.2][:len(path_x)]  # Adjust the opacity length to visible path length

#             # Update the robot's path and position
#             for trace in fig.data:
#                 if trace.name == f'{robot_name} Path':
#                     trace.x = path_x
#                     trace.y = path_y
#                     trace.marker = dict(size=6, opacity=opacities)
#                 elif trace.name == robot_name:
#                     trace.x = [robot_positions_current[robot_name][0]]
#                     trace.y = [robot_positions_current[robot_name][1]]
            
#             # Display the updated map
#             with map_placeholder:
#                 st.plotly_chart(fig)
    
#             # Display communication messages
#             with chat_placeholder:
#                 st.markdown(f"**{robot_name}:**")
#                 if robot_positions_current[robot_name] in messages:
#                     st.markdown(messages[robot_positions_current[robot_name]], unsafe_allow_html=True)
#                 else:
#                     st.empty()

#             # Wait for a while to simulate real-time movement
#             time.sleep(1)



# import streamlit as st
# import plotly.graph_objects as go
# import time
# import random

# def generate_intermediate_path(start, end):
#     path = [start]
#     x1, y1 = start
#     x2, y2 = end
#     while (x1, y1) != (x2, y2):
#         if x1 < x2:
#             x1 += 1
#         elif x1 > x2:
#             x1 -= 1
#         if y1 < y2:
#             y1 += 1
#         elif y1 > y2:
#             y1 -= 1
#         path.append((x1, y1))
#     return path

# def generate_messages(path, robot_name, color):
#     messages = {}
#     num_points = len(path)
#     intervals = max(1, num_points // 6)  # Messages at every sixth of the path
#     for i in range(1, num_points):
#         if i % intervals == 0:
#             messages[path[i]] = f"<b>Alert! <span style='color:{color};'>{robot_name}</span> is delayed and has reached {path[i]}.</b>"
#     if path[-1] not in messages:
#         messages[path[-1]] = f"<b><span style='color:{color};'>{robot_name}</span> has reached its destination at {path[-1]}.</b>"
#     return messages

# def generate_obstacles(num_obstacles, robot_paths):
#     obstacles = []
#     for _ in range(num_obstacles):
#         x = random.randint(0, 50)
#         y = random.randint(0, 50)
#         if any((x, y) in path for path in robot_paths):
#             continue  # Skip if obstacle is on a robot's path
#         obstacles.append((x, y))
#     return obstacles

# # Define robots' start and end positions
# robot_positions = {
#     "Explorer Robot": {"start": (1, 1), "end": (25, 10)},
#     "Scout Robot": {"start": (14, 15), "end": (48, 35)},
#     "Surveyor Robot": {"start": (30, 26), "end": (47, 48)},
#     "Drone Robot": {"start": (4, 7), "end": (24, 35)}
# }

# # Define colors for robots
# colors = {
#     "Explorer Robot": "blue",
#     "Scout Robot": "green",
#     "Surveyor Robot": "purple",
#     "Drone Robot": "red"
# }

# # Create robots dictionary with paths, colors, and messages
# robots = {}
# all_paths = []
# for robot_name, pos in robot_positions.items():
#     path = generate_intermediate_path(pos["start"], pos["end"])
#     all_paths.append(path)
#     robots[robot_name] = {
#         "path": path,
#         "color": colors[robot_name],
#         "messages": generate_messages(path, robot_name, colors[robot_name])
#     }

# # Generate obstacles
# num_obstacles = 50
# obstacles = generate_obstacles(num_obstacles, all_paths)

# # Create a Plotly figure for the map
# fig = go.Figure()

# # Add obstacles to the map in a single trace
# obstacle_x, obstacle_y = zip(*obstacles) if obstacles else ([], [])
# fig.add_trace(go.Scatter(
#     x=obstacle_x, 
#     y=obstacle_y, 
#     mode='markers', 
#     marker=dict(size=10, color='brown', symbol='cross'), 
#     name='Obstacle'
# ))

# # Add the robots' paths and positions with enhanced styling
# for robot_name, robot_data in robots.items():
#     path = robot_data["path"]
#     color = robot_data["color"]
#     messages = robot_data["messages"]
    
#     fig.add_trace(go.Scatter(x=[], y=[], mode='lines+markers', line=dict(color=color, dash='dot'), marker=dict(size=6), name=f'{robot_name} Path'))
    
#     robot_position = path[0]
#     fig.add_trace(go.Scatter(
#         x=[robot_position[0]], 
#         y=[robot_position[1]], 
#         mode='markers+text', 
#         marker=dict(size=15, color=color, symbol='circle', line=dict(width=2, color='black')), 
#         text=[robot_name], 
#         textposition='top center', 
#         name=robot_name
#     ))

# fig.update_layout(
#     title='Enhanced Robots Navigation Map with Obstacles',
#     xaxis=dict(range=[0, 50], autorange=False, title='X Coordinate'),
#     yaxis=dict(range=[0, 50], autorange=False, title='Y Coordinate'),
#     width=1200,
#     height=900,
#     paper_bgcolor='lightgrey',  # Changed to light grey
#     plot_bgcolor='white',
#     showlegend=True
# )

# # Layout: Map above, Chat below
# map_placeholder = st.empty()
# chat_placeholder = st.empty()

# # Button to control movement
# if st.button('Acknowledge'):
#     st.session_state.paused = not st.session_state.paused
# else:
#     if 'paused' not in st.session_state:
#         st.session_state.paused = False

# # JavaScript for blinking text
# st.markdown("""
#     <style>
#     @keyframes blinker {
#         50% { opacity: 0; }
#     }
#     .blinking {
#         animation: blinker 1s linear infinite;
#     }
#     </style>
#     """, unsafe_allow_html=True)

# # Simulate robots' movement
# robot_positions_current = {name: data["path"][0] for name, data in robots.items()}
# while any(pos != path[-1] for name, (path, pos) in zip(robots.keys(), zip([data["path"] for data in robots.values()], robot_positions_current.values()))):
#     if not st.session_state.paused:
#         for robot_name, robot_data in robots.items():
#             path = robot_data["path"]
#             color = robot_data["color"]
#             messages = robot_data["messages"]
            
#             current_pos_index = path.index(robot_positions_current[robot_name])
#             if current_pos_index < len(path) - 1:
#                 robot_positions_current[robot_name] = path[current_pos_index + 1]
                
#                 # Update the visible part of the path
#                 start_index = max(0, current_pos_index - 2)
#                 end_index = min(len(path), current_pos_index + 3)
#                 visible_path = path[start_index:end_index]
#                 path_x, path_y = zip(*visible_path)

#                 # Set opacities for fading effect
#                 opacities = [0.2, 0.5, 1.0, 0.5, 0.2][:len(path_x)]  # Adjust the opacity length to visible path length

#                 # Update the robot's path and position
#                 for trace in fig.data:
#                     if trace.name == f'{robot_name} Path':
#                         trace.x = path_x
#                         trace.y = path_y
#                         trace.marker = dict(size=6, opacity=opacities)
#                     elif trace.name == robot_name:
#                         trace.x = [robot_positions_current[robot_name][0]]
#                         trace.y = [robot_positions_current[robot_name][1]]
                
#                 # Display the updated map
#                 with map_placeholder:
#                     st.plotly_chart(fig)
        
#                 # Display communication messages
#                 with chat_placeholder:
#                     st.markdown(f"<div class='blinking'>**{robot_name}:**</div>", unsafe_allow_html=True)
#                     if robot_positions_current[robot_name] in messages:
#                         st.markdown(messages[robot_positions_current[robot_name]], unsafe_allow_html=True)
#                     else:
#                         st.empty()

#                 # Wait for a while to simulate real-time movement
#                 time.sleep(1)
#     else:
#         # Display paused message
#         with map_placeholder:
#             st.plotly_chart(fig)
#         with chat_placeholder:
#             st.markdown("<div class='blinking'><b>Movement Paused. Click 'Acknowledge' to Resume.</b></div>", unsafe_allow_html=True)
#         time.sleep(1)



# #Final_working
# import streamlit as st
# import plotly.graph_objects as go
# import time
# import random

# def generate_intermediate_path(start, end):
#     path = [start]
#     x1, y1 = start
#     x2, y2 = end
#     while (x1, y1) != (x2, y2):
#         if x1 < x2:
#             x1 += 1
#         elif x1 > x2:
#             x1 -= 1
#         if y1 < y2:
#             y1 += 1
#         elif y1 > y2:
#             y1 -= 1
#         path.append((x1, y1))
#     return path

# def generate_messages(path, robot_name, color):
#     messages = {}
#     num_points = len(path)
#     intervals = max(1, num_points // 6)  # Messages at every sixth of the path
#     for i in range(1, num_points):
#         if i % intervals == 0:
#             messages[path[i]] = f"<b>Alert! <span style='color:{color};'>{robot_name}</span> is delayed and has reached {path[i]}.</b>"
#     if path[-1] not in messages:
#         messages[path[-1]] = f"<b><span style='color:{color};'>{robot_name}</span> has reached its destination at {path[-1]}.</b>"
#     return messages

# def generate_obstacles(num_obstacles, robot_paths):
#     obstacles = []
#     for _ in range(num_obstacles):
#         x = random.randint(0, 50)
#         y = random.randint(0, 50)
#         if any((x, y) in path for path in robot_paths):
#             continue  # Skip if obstacle is on a robot's path
#         obstacles.append((x, y))
#     return obstacles

# # Define robots' start and end positions
# robot_positions = {
#     "Explorer Robot": {"start": (1, 1), "end": (25, 10)},
#     "Scout Robot": {"start": (14, 15), "end": (48, 35)},
#     "Surveyor Robot": {"start": (30, 26), "end": (47, 48)},
#     "Drone Robot": {"start": (4, 7), "end": (24, 35)}
# }

# # Define colors for robots
# colors = {
#     "Explorer Robot": "blue",
#     "Scout Robot": "green",
#     "Surveyor Robot": "purple",
#     "Drone Robot": "red"
# }

# # Create robots dictionary with paths, colors, and messages
# robots = {}
# all_paths = []
# for robot_name, pos in robot_positions.items():
#     path = generate_intermediate_path(pos["start"], pos["end"])
#     all_paths.append(path)
#     robots[robot_name] = {
#         "path": path,
#         "color": colors[robot_name],
#         "messages": generate_messages(path, robot_name, colors[robot_name])
#     }

# # Generate obstacles
# num_obstacles = 50
# obstacles = generate_obstacles(num_obstacles, all_paths)

# # Create a Plotly figure for the map
# fig = go.Figure()

# # Add obstacles to the map in a single trace
# obstacle_x, obstacle_y = zip(*obstacles) if obstacles else ([], [])
# fig.add_trace(go.Scatter(
#     x=obstacle_x, 
#     y=obstacle_y, 
#     mode='markers', 
#     marker=dict(size=10, color='brown', symbol='cross'), 
#     name='Obstacle'
# ))

# # Add the robots' paths and positions with enhanced styling
# for robot_name, robot_data in robots.items():
#     path = robot_data["path"]
#     color = robot_data["color"]
#     messages = robot_data["messages"]
    
#     fig.add_trace(go.Scatter(x=[], y=[], mode='lines+markers', line=dict(color=color, dash='dot'), marker=dict(size=6), name=f'{robot_name} Path'))
    
#     robot_position = path[0]
#     fig.add_trace(go.Scatter(
#         x=[robot_position[0]], 
#         y=[robot_position[1]], 
#         mode='markers+text', 
#         marker=dict(size=15, color=color, symbol='circle', line=dict(width=2, color='black')), 
#         text=[robot_name], 
#         textposition='top center', 
#         name=robot_name
#     ))

# fig.update_layout(
#     title='Enhanced Robots Navigation Map with Obstacles',
#     xaxis=dict(range=[0, 50], autorange=False, title='X Coordinate'),
#     yaxis=dict(range=[0, 50], autorange=False, title='Y Coordinate'),
#     width=1200,
#     height=900,
#     paper_bgcolor='lightgrey',  # Changed to light grey
#     plot_bgcolor='white',
#     showlegend=True
# )

# # Layout: Map above, Chat below
# map_placeholder = st.empty()
# chat_placeholder = st.empty()

# # Button to control movement
# if st.button('Acknowledge'):
#     st.session_state.paused = not st.session_state.paused
# else:
#     if 'paused' not in st.session_state:
#         st.session_state.paused = False

# # JavaScript for blinking text
# st.markdown("""
#     <style>
#     @keyframes blinker {
#         50% { opacity: 0; }
#     }
#     .blinking {
#         animation: blinker 1s linear infinite;
#     }
#     </style>
#     """, unsafe_allow_html=True)

# # Simulate robots' movement
# robot_positions_current = {name: data["path"][0] for name, data in robots.items()}
# while any(pos != path[-1] for name, (path, pos) in zip(robots.keys(), zip([data["path"] for data in robots.values()], robot_positions_current.values()))):
#     if not st.session_state.paused:
#         for robot_name, robot_data in robots.items():
#             path = robot_data["path"]
#             color = robot_data["color"]
#             messages = robot_data["messages"]
            
#             current_pos_index = path.index(robot_positions_current[robot_name])
#             if current_pos_index < len(path) - 1:
#                 robot_positions_current[robot_name] = path[current_pos_index + 1]
                
#                 # Update the visible part of the path
#                 start_index = max(0, current_pos_index - 2)
#                 end_index = min(len(path), current_pos_index + 3)
#                 visible_path = path[start_index:end_index]
#                 path_x, path_y = zip(*visible_path)

#                 # Set opacities for fading effect
#                 opacities = [0.2, 0.5, 1.0, 0.5, 0.2][:len(path_x)]  # Adjust the opacity length to visible path length

#                 # Update the robot's path and position
#                 for trace in fig.data:
#                     if trace.name == f'{robot_name} Path':
#                         trace.x = path_x
#                         trace.y = path_y
#                         trace.marker = dict(size=6, opacity=opacities)
#                     elif trace.name == robot_name:
#                         trace.x = [robot_positions_current[robot_name][0]]
#                         trace.y = [robot_positions_current[robot_name][1]]
                
#                 # Display the updated map
#                 with map_placeholder:
#                     st.plotly_chart(fig)
        
#                 # Display communication messages
#                 with chat_placeholder:
#                     st.markdown(f"<div class='blinking'>**{robot_name}:**</div>", unsafe_allow_html=True)
#                     if robot_positions_current[robot_name] in messages:
#                         st.markdown(messages[robot_positions_current[robot_name]], unsafe_allow_html=True)
#                     else:
#                         st.empty()

#                 # Wait for a while to simulate real-time movement
#                 time.sleep(1)
#     else:
#         # Display paused message
#         with map_placeholder:
#             st.plotly_chart(fig)
#         with chat_placeholder:
#             st.markdown("<div class='blinking'><b>Movement Paused. Click 'Acknowledge' to Resume.</b></div>", unsafe_allow_html=True)
#         time.sleep(1)



# # TREE
# import streamlit as st
# import plotly.graph_objects as go
# import time
# import random
# from PIL import Image

# def generate_intermediate_path(start, end):
#     path = [start]
#     x1, y1 = start
#     x2, y2 = end
#     while (x1, y1) != (x2, y2):
#         if x1 < x2:
#             x1 += 1
#         elif x1 > x2:
#             x1 -= 1
#         if y1 < y2:
#             y1 += 1
#         elif y1 > y2:
#             y1 -= 1
#         path.append((x1, y1))
#     return path

# def generate_messages(path, robot_name, color):
#     messages = {}
#     num_points = len(path)
#     intervals = max(1, num_points // 6)
#     for i in range(1, num_points):
#         if i % intervals == 0:
#             messages[path[i]] = f"<b>Alert! <span style='color:{color};'>{robot_name}</span> is delayed and has reached {path[i]}.</b>"
#     if path[-1] not in messages:
#         messages[path[-1]] = f"<b><span style='color:{color};'>{robot_name}</span> has reached its destination at {path[-1]}.</b>"
#     return messages

# def generate_obstacles(num_obstacles, robot_paths):
#     obstacles = []
#     for _ in range(num_obstacles):
#         x = random.randint(0, 50)
#         y = random.randint(0, 50)
#         if any((x, y) in path for path in robot_paths):
#             continue
#         obstacles.append((x, y))
#     return obstacles

# # Define robots' start and end positions
# robot_positions = {
#     "Explorer Robot": {"start": (1, 1), "end": (25, 10)},
#     "Scout Robot": {"start": (14, 15), "end": (48, 35)},
#     "Surveyor Robot": {"start": (30, 26), "end": (47, 48)},
#     "Drone Robot": {"start": (4, 7), "end": (24, 35)}
# }

# # Define colors for robots
# colors = {
#     "Explorer Robot": "blue",
#     "Scout Robot": "green",
#     "Surveyor Robot": "purple",
#     "Drone Robot": "red"
# }

# # Create robots dictionary with paths, colors, and messages
# robots = {}
# all_paths = []
# for robot_name, pos in robot_positions.items():
#     path = generate_intermediate_path(pos["start"], pos["end"])
#     all_paths.append(path)
#     robots[robot_name] = {
#         "path": path,
#         "color": colors[robot_name],
#         "messages": generate_messages(path, robot_name, colors[robot_name])
#     }

# # Generate obstacles
# num_obstacles = 50
# obstacles = generate_obstacles(num_obstacles, all_paths)

# # Create a Plotly figure for the map
# fig = go.Figure()

# # Add the tree image as obstacles
# tree_img = Image.open('tree.png')
# for x, y in obstacles:
#     fig.add_layout_image(
#         source=tree_img,
#         x=x - 0.5,
#         y=y + 0.5,
#         xref="x",
#         yref="y",
#         sizex=2,
#         sizey=2,
#         xanchor="center",
#         yanchor="middle"
#     )

# # Add the robots' paths and positions with enhanced styling
# for robot_name, robot_data in robots.items():
#     path = robot_data["path"]
#     color = robot_data["color"]
#     messages = robot_data["messages"]
    
#     fig.add_trace(go.Scatter(x=[], y=[], mode='lines+markers', line=dict(color=color, dash='dot'), marker=dict(size=6), name=f'{robot_name} Path'))
    
#     robot_position = path[0]
#     fig.add_trace(go.Scatter(
#         x=[robot_position[0]], 
#         y=[robot_position[1]], 
#         mode='markers+text', 
#         marker=dict(size=15, color=color, symbol='circle', line=dict(width=2, color='black')), 
#         text=[robot_name], 
#         textposition='top center', 
#         name=robot_name
#     ))

# fig.update_layout(
#     title='Enhanced Robots Navigation Map with Tree Obstacles',
#     xaxis=dict(range=[0, 50], autorange=False, title='X Coordinate'),
#     yaxis=dict(range=[0, 50], autorange=False, title='Y Coordinate'),
#     width=1200,
#     height=900,
#     paper_bgcolor='lightgrey',
#     plot_bgcolor='white',
#     showlegend=True
# )

# # Layout: Map above, Chat below
# map_placeholder = st.empty()
# chat_placeholder = st.empty()

# # Button to control movement
# if st.button('Acknowledge'):
#     st.session_state.paused = not st.session_state.paused
# else:
#     if 'paused' not in st.session_state:
#         st.session_state.paused = False







# # JavaScript for blinking text
# st.markdown("""
#     <style>
#     @keyframes blinker {
#         50% { opacity: 0; }
#     }
#     .blinking {
#         animation: blinker 1s linear infinite;
#     }
#     </style>
#     """, unsafe_allow_html=True)



# # Simulate robots' movement
# robot_positions_current = {name: data["path"][0] for name, data in robots.items()}
# while any(pos != path[-1] for name, (path, pos) in zip(robots.keys(), zip([data["path"] for data in robots.values()], robot_positions_current.values()))):
#     if not st.session_state.paused:
#         for robot_name, robot_data in robots.items():
#             path = robot_data["path"]
#             color = robot_data["color"]
#             messages = robot_data["messages"]
            
#             current_pos_index = path.index(robot_positions_current[robot_name])
#             if current_pos_index < len(path) - 1:
#                 robot_positions_current[robot_name] = path[current_pos_index + 1]
                
#                 # Update the visible part of the path
#                 start_index = max(0, current_pos_index - 2)
#                 end_index = min(len(path), current_pos_index + 3)
#                 visible_path = path[start_index:end_index]
#                 path_x, path_y = zip(*visible_path)

#                 # Set opacities for fading effect
#                 opacities = [0.2, 0.5, 1.0, 0.5, 0.2][:len(path_x)]

#                 # Update the robot's path and position
#                 for trace in fig.data:
#                     if trace.name == f'{robot_name} Path':
#                         trace.x = path_x
#                         trace.y = path_y
#                         trace.marker = dict(size=6, opacity=opacities)
#                     elif trace.name == robot_name:
#                         trace.x = [robot_positions_current[robot_name][0]]
#                         trace.y = [robot_positions_current[robot_name][1]]
                
#                 # Display the updated map
#                 with map_placeholder:
#                     st.plotly_chart(fig)
        
#                 # Display communication messages
#                 with chat_placeholder:
#                     st.markdown(f"<div class='blinking'>**{robot_name}:**</div>", unsafe_allow_html=True)
#                     if robot_positions_current[robot_name] in messages:
#                         st.markdown(messages[robot_positions_current[robot_name]], unsafe_allow_html=True)
#                     else:
#                         st.empty()

#                 # Wait for a while to simulate real-time movement
#                 time.sleep(1)
#     else:
#         # Display paused message
#         with map_placeholder:
#             st.plotly_chart(fig)
#         with chat_placeholder:
#             st.markdown("<div class='blinking'><b>Movement Paused. Click 'Acknowledge' to Resume.</b></div>", unsafe_allow_html=True)
#         time.sleep(1)



# # camera placeholder below 1.
# import streamlit as st
# import plotly.graph_objects as go
# import time
# import random
# from PIL import Image

# def generate_intermediate_path(start, end):
#     path = [start]
#     x1, y1 = start
#     x2, y2 = end
#     while (x1, y1) != (x2, y2):
#         if x1 < x2:
#             x1 += 1
#         elif x1 > x2:
#             x1 -= 1
#         if y1 < y2:
#             y1 += 1
#         elif y1 > y2:
#             y1 -= 1
#         path.append((x1, y1))
#     return path

# def generate_messages(path, robot_name, color):
#     messages = {}
#     num_points = len(path)
#     intervals = max(1, num_points // 6)
#     for i in range(1, num_points):
#         if i % intervals == 0:
#             messages[path[i]] = f"<b>Alert! <span style='color:{color};'>{robot_name}</span> is delayed and has reached {path[i]}.</b>"
#     if path[-1] not in messages:
#         messages[path[-1]] = f"<b><span style='color:{color};'>{robot_name}</span> has reached its destination at {path[-1]}.</b>"
#     return messages

# def generate_obstacles(num_obstacles, robot_paths):
#     obstacles = []
#     for _ in range(num_obstacles):
#         x = random.randint(0, 50)
#         y = random.randint(0, 50)
#         if any((x, y) in path for path in robot_paths):
#             continue
#         obstacles.append((x, y))
#     return obstacles

# # Define robots' start and end positions
# robot_positions = {
#     "Explorer Robot": {"start": (1, 1), "end": (25, 10)},
#     "Scout Robot": {"start": (14, 15), "end": (48, 35)},
#     "Surveyor Robot": {"start": (30, 26), "end": (47, 48)},
#     "Drone Robot": {"start": (4, 7), "end": (24, 35)}
# }

# # Define colors for robots
# colors = {
#     "Explorer Robot": "blue",
#     "Scout Robot": "green",
#     "Surveyor Robot": "purple",
#     "Drone Robot": "red"
# }

# # Create robots dictionary with paths, colors, and messages
# robots = {}
# all_paths = []
# for robot_name, pos in robot_positions.items():
#     path = generate_intermediate_path(pos["start"], pos["end"])
#     all_paths.append(path)
#     robots[robot_name] = {
#         "path": path,
#         "color": colors[robot_name],
#         "messages": generate_messages(path, robot_name, colors[robot_name])
#     }

# # Generate obstacles
# num_obstacles = 50
# obstacles = generate_obstacles(num_obstacles, all_paths)

# # Create a Plotly figure for the map
# fig = go.Figure()

# # Add the tree image as obstacles
# tree_img = Image.open('tree.png')
# for x, y in obstacles:
#     fig.add_layout_image(
#         source=tree_img,
#         x=x - 0.5,
#         y=y + 0.5,
#         xref="x",
#         yref="y",
#         sizex=2,
#         sizey=2,
#         xanchor="center",
#         yanchor="middle"
#     )

# # Add the robots' paths and positions with enhanced styling
# for robot_name, robot_data in robots.items():
#     path = robot_data["path"]
#     color = robot_data["color"]
#     messages = robot_data["messages"]
    
#     fig.add_trace(go.Scatter(x=[], y=[], mode='lines+markers', line=dict(color=color, dash='dot'), marker=dict(size=6), name=f'{robot_name} Path'))
    
#     robot_position = path[0]
#     fig.add_trace(go.Scatter(
#         x=[robot_position[0]], 
#         y=[robot_position[1]], 
#         mode='markers+text', 
#         marker=dict(size=15, color=color, symbol='circle', line=dict(width=2, color='black')), 
#         text=[robot_name], 
#         textposition='top center', 
#         name=robot_name
#     ))

# fig.update_layout(
#     title='Enhanced Robots Navigation Map with Tree Obstacles',
#     xaxis=dict(range=[0, 50], autorange=False, title='X Coordinate'),
#     yaxis=dict(range=[0, 50], autorange=False, title='Y Coordinate'),
#     width=1200,
#     height=900,
#     paper_bgcolor='lightgrey',
#     plot_bgcolor='white',
#     showlegend=True
# )

# # Layout: Map above, Chat below, and Robot's View section
# map_placeholder = st.empty()
# chat_placeholder = st.empty()
# robot_view_placeholder = st.empty()  # Placeholder for the Robot's View section

# # Button to control movement
# if st.button('Acknowledge'):
#     st.session_state.paused = not st.session_state.paused
# else:
#     if 'paused' not in st.session_state:
#         st.session_state.paused = False

# # JavaScript for blinking text
# st.markdown("""
#     <style>
#     @keyframes blinker {
#         50% { opacity: 0; }
#     }
#     .blinking {
#         animation: blinker 1s linear infinite;
#     }
#     </style>
#     """, unsafe_allow_html=True)

# # Display the Robot's View section with the static image
# with robot_view_placeholder:
#     st.subheader("Robot's View")
#     robot_view_image = Image.open('sim.png')
#     st.image(robot_view_image, caption="Placeholder for Robot's View", use_column_width=True)

# # Simulate robots' movement
# robot_positions_current = {name: data["path"][0] for name, data in robots.items()}
# while any(pos != path[-1] for name, (path, pos) in zip(robots.keys(), zip([data["path"] for data in robots.values()], robot_positions_current.values()))):
#     if not st.session_state.paused:
#         for robot_name, robot_data in robots.items():
#             path = robot_data["path"]
#             color = robot_data["color"]
#             messages = robot_data["messages"]
            
#             current_pos_index = path.index(robot_positions_current[robot_name])
#             if current_pos_index < len(path) - 1:
#                 robot_positions_current[robot_name] = path[current_pos_index + 1]
                
#                 # Update the visible part of the path
#                 start_index = max(0, current_pos_index - 2)
#                 end_index = min(len(path), current_pos_index + 3)
#                 visible_path = path[start_index:end_index]
#                 path_x, path_y = zip(*visible_path)

#                 # Set opacities for fading effect
#                 opacities = [0.2, 0.5, 1.0, 0.5, 0.2][:len(path_x)]

#                 # Update the robot's path and position
#                 for trace in fig.data:
#                     if trace.name == f'{robot_name} Path':
#                         trace.x = path_x
#                         trace.y = path_y
#                         trace.marker = dict(size=6, opacity=opacities)
#                     elif trace.name == robot_name:
#                         trace.x = [robot_positions_current[robot_name][0]]
#                         trace.y = [robot_positions_current[robot_name][1]]
                
#                 # Display the updated map
#                 with map_placeholder:
#                     st.plotly_chart(fig)
        
#                 # Display communication messages
#                 with chat_placeholder:
#                     st.markdown(f"<div class='blinking'>**{robot_name}:**</div>", unsafe_allow_html=True)
#                     if robot_positions_current[robot_name] in messages:
#                         st.markdown(messages[robot_positions_current[robot_name]], unsafe_allow_html=True)
#                     else:
#                         st.empty()

#                 # Wait for a while to simulate real-time movement
#                 time.sleep(1)
#     else:
#         # Display paused message
#         with map_placeholder:
#             st.plotly_chart(fig)
#         with chat_placeholder:
#             st.markdown("<div class='blinking'><b>Movement Paused. Click 'Acknowledge' to Resume.</b></div>", unsafe_allow_html=True)
#         time.sleep(1)


# #Final
# import streamlit as st
# import plotly.graph_objects as go
# import time
# import random
# from PIL import Image

# def generate_intermediate_path(start, end):
#     path = [start]
#     x1, y1 = start
#     x2, y2 = end
#     while (x1, y1) != (x2, y2):
#         if x1 < x2:
#             x1 += 1
#         elif x1 > x2:
#             x1 -= 1
#         if y1 < y2:
#             y1 += 1
#         elif y1 > y2:
#             y1 -= 1
#         path.append((x1, y1))
#     return path

# def generate_messages(path, robot_name, color):
#     messages = {}
#     num_points = len(path)
#     intervals = max(1, num_points // 6)
#     for i in range(1, num_points):
#         if i % intervals == 0:
#             messages[path[i]] = f"<b>Alert! <span style='color:{color};'>{robot_name}</span> is delayed and has reached {path[i]}.</b>"
#     if path[-1] not in messages:
#         messages[path[-1]] = f"<b><span style='color:{color};'>{robot_name}</span> has reached its destination at {path[-1]}.</b>"
#     return messages

# def generate_obstacles(num_obstacles, robot_paths):
#     obstacles = []
#     for _ in range(num_obstacles):
#         x = random.randint(0, 50)
#         y = random.randint(0, 50)
#         if any((x, y) in path for path in robot_paths):
#             continue
#         obstacles.append((x, y))
#     return obstacles

# # Define robots' start and end positions
# robot_positions = {
#     "Explorer Robot": {"start": (1, 1), "end": (25, 10)},
#     "Scout Robot": {"start": (14, 15), "end": (48, 35)},
#     "Surveyor Robot": {"start": (30, 26), "end": (47, 48)},
#     "Drone Robot": {"start": (4, 7), "end": (24, 35)}
# }

# # Define colors for robots
# colors = {
#     "Explorer Robot": "blue",
#     "Scout Robot": "green",
#     "Surveyor Robot": "purple",
#     "Drone Robot": "red"
# }

# # Create robots dictionary with paths, colors, and messages
# robots = {}
# all_paths = []
# for robot_name, pos in robot_positions.items():
#     path = generate_intermediate_path(pos["start"], pos["end"])
#     all_paths.append(path)
#     robots[robot_name] = {
#         "path": path,
#         "color": colors[robot_name],
#         "messages": generate_messages(path, robot_name, colors[robot_name])
#     }

# # Generate obstacles
# num_obstacles = 50
# obstacles = generate_obstacles(num_obstacles, all_paths)

# # Create a Plotly figure for the map
# fig = go.Figure()

# # Add the tree image as obstacles
# tree_img = Image.open('tree.png')
# for x, y in obstacles:
#     fig.add_layout_image(
#         source=tree_img,
#         x=x - 0.5,
#         y=y + 0.5,
#         xref="x",
#         yref="y",
#         sizex=2,
#         sizey=2,
#         xanchor="center",
#         yanchor="middle"
#     )

# # Add the robots' paths and positions with enhanced styling
# for robot_name, robot_data in robots.items():
#     path = robot_data["path"]
#     color = robot_data["color"]
#     messages = robot_data["messages"]
    
#     fig.add_trace(go.Scatter(x=[], y=[], mode='lines+markers', line=dict(color=color, dash='dot'), marker=dict(size=6), name=f'{robot_name} Path'))
    
#     robot_position = path[0]
#     fig.add_trace(go.Scatter(
#         x=[robot_position[0]], 
#         y=[robot_position[1]], 
#         mode='markers+text', 
#         marker=dict(size=15, color=color, symbol='circle', line=dict(width=2, color='black')), 
#         text=[robot_name], 
#         textposition='top center', 
#         name=robot_name
#     ))

# fig.update_layout(
#     title='Enhanced Robots Navigation Map with Tree Obstacles',
#     xaxis=dict(range=[0, 50], autorange=False, title='X Coordinate'),
#     yaxis=dict(range=[0, 50], autorange=False, title='Y Coordinate'),
#     width=900,
#     height=700,
#     paper_bgcolor='lightgrey',
#     plot_bgcolor='white',
#     showlegend=True
# )

# # Layout: Map and chat in the left column, image in the right column
# col1, col2 = st.columns([10, 3])

# with col1:
#     # Map and chat section
#     map_placeholder = st.empty()
#     chat_placeholder = st.empty()

# with col2:
#     # Robot's view section
#     st.subheader("Simulation Overview")
#     sim_image = Image.open('sim.png')
#     st.image(sim_image, caption="Robot's Point of View", use_column_width=True)

# # Button to control movement
# if st.button('Acknowledge'):
#     st.session_state.paused = not st.session_state.paused
# else:
#     if 'paused' not in st.session_state:
#         st.session_state.paused = False


# # JavaScript for blinking text
# st.markdown("""
#     <style>
#     @keyframes blinker {
#         50% { opacity: 0; }
#     }
#     .blinking {
#         animation: blinker 1s linear infinite;
#     }
#     </style>
#     """, unsafe_allow_html=True)

# # Simulate robots' movement
# robot_positions_current = {name: data["path"][0] for name, data in robots.items()}
# while any(pos != path[-1] for name, (path, pos) in zip(robots.keys(), zip([data["path"] for data in robots.values()], robot_positions_current.values()))):
#     if not st.session_state.paused:
#         for robot_name, robot_data in robots.items():
#             path = robot_data["path"]
#             color = robot_data["color"]
#             messages = robot_data["messages"]
            
#             current_pos_index = path.index(robot_positions_current[robot_name])
#             if current_pos_index < len(path) - 1:
#                 robot_positions_current[robot_name] = path[current_pos_index + 1]
                
#                 # Update the visible part of the path
#                 start_index = max(0, current_pos_index - 2)
#                 end_index = min(len(path), current_pos_index + 3)
#                 visible_path = path[start_index:end_index]
#                 path_x, path_y = zip(*visible_path)

#                 # Set opacities for fading effect
#                 opacities = [0.2, 0.5, 1.0, 0.5, 0.2][:len(path_x)]

#                 # Update the robot's path and position
#                 for trace in fig.data:
#                     if trace.name == f'{robot_name} Path':
#                         trace.x = path_x
#                         trace.y = path_y
#                         trace.marker = dict(size=6, opacity=opacities)
#                     elif trace.name == robot_name:
#                         trace.x = [robot_positions_current[robot_name][0]]
#                         trace.y = [robot_positions_current[robot_name][1]]
                
#                 # Display the updated map
#                 with map_placeholder:
#                     st.plotly_chart(fig)
        
#                 # Display communication messages
#                 with chat_placeholder:
#                     st.markdown(f"<div class='blinking'>**{robot_name}:**</div>", unsafe_allow_html=True)
#                     if robot_positions_current[robot_name] in messages:
#                         st.markdown(messages[robot_positions_current[robot_name]], unsafe_allow_html=True)
#                     else:
#                         st.empty()

#                 # Wait for a while to simulate real-time movement
#                 time.sleep(1)
#     else:
#         # Display paused message
#         with map_placeholder:
#             st.plotly_chart(fig)
#         with chat_placeholder:
#             st.markdown("<div class='blinking'><b>Movement Paused. Click 'Acknowledge' to Resume.</b></div>", unsafe_allow_html=True)
#         time.sleep(1)

import streamlit as st
import plotly.graph_objects as go
import time
import random
from PIL import Image

def generate_intermediate_path(start, end):
    path = [start]
    x1, y1 = start
    x2, y2 = end
    while (x1, y1) != (x2, y2):
        if x1 < x2:
            x1 += 1
        elif x1 > x2:
            x1 -= 1
        if y1 < y2:
            y1 += 1
        elif y1 > y2:
            y1 -= 1
        path.append((x1, y1))
    return path

def generate_messages(path, robot_name, color):
    messages = {}
    num_points = len(path)
    intervals = max(1, num_points // 6)
    for i in range(1, num_points):
        if i % intervals == 0:
            messages[path[i]] = f"<b>Alert! <span style='color:{color};'>{robot_name}</span> is delayed and has reached {path[i]}.</b>"
    if path[-1] not in messages:
        messages[path[-1]] = f"<b><span style='color:{color};'>{robot_name}</span> has reached its destination at {path[-1]}.</b>"
    return messages

def generate_obstacles(num_obstacles, robot_paths):
    obstacles = []
    for _ in range(num_obstacles):
        x = random.randint(0, 50)
        y = random.randint(0, 50)
        if any((x, y) in path for path in robot_paths):
            continue
        obstacles.append((x, y))
    return obstacles

# Define robots' start and end positions
robot_positions = {
    "Explorer Robot": {"start": (1, 1), "end": (25, 10)},
    "Scout Robot": {"start": (14, 15), "end": (48, 35)},
    "Surveyor Robot": {"start": (30, 26), "end": (47, 48)},
    "Drone Robot": {"start": (4, 7), "end": (24, 35)}
}

# Define colors for robots
colors = {
    "Explorer Robot": "blue",
    "Scout Robot": "green",
    "Surveyor Robot": "purple",
    "Drone Robot": "red"
}

# Create robots dictionary with paths, colors, and messages
robots = {}
all_paths = []
for robot_name, pos in robot_positions.items():
    path = generate_intermediate_path(pos["start"], pos["end"])
    all_paths.append(path)
    robots[robot_name] = {
        "path": path,
        "color": colors[robot_name],
        "messages": generate_messages(path, robot_name, colors[robot_name])
    }

# Generate obstacles
num_obstacles = 50
obstacles = generate_obstacles(num_obstacles, all_paths)

# Create a Plotly figure for the map
fig = go.Figure()

# Add the tree image as obstacles
tree_img = Image.open('tree.png')
for x, y in obstacles:
    fig.add_layout_image(
        source=tree_img,
        x=x - 0.5,
        y=y + 0.5,
        xref="x",
        yref="y",
        sizex=2,
        sizey=2,
        xanchor="center",
        yanchor="middle"
    )

# Add the robots' paths and positions with enhanced styling
for robot_name, robot_data in robots.items():
    path = robot_data["path"]
    color = robot_data["color"]
    messages = robot_data["messages"]
    
    fig.add_trace(go.Scatter(x=[], y=[], mode='lines+markers', line=dict(color=color, dash='dot'), marker=dict(size=6), name=f'{robot_name} Path'))
    
    robot_position = path[0]
    fig.add_trace(go.Scatter(
        x=[robot_position[0]], 
        y=[robot_position[1]], 
        mode='markers+text', 
        marker=dict(size=15, color=color, symbol='circle', line=dict(width=2, color='black')), 
        text=[robot_name], 
        textposition='top center', 
        name=robot_name
    ))

fig.update_layout(
    title='Enhanced Robots Navigation Map with Tree Obstacles',
    xaxis=dict(range=[0, 50], autorange=False, title='X Coordinate'),
    yaxis=dict(range=[0, 50], autorange=False, title='Y Coordinate'),
    width=900,
    height=700,
    paper_bgcolor='lightgrey',
    plot_bgcolor='white',
    showlegend=True
)

# Layout: Map and chat in the left column, image in the right column
col1, col2 = st.columns([10, 3])

with col1:
    # Map and chat section
    map_placeholder = st.empty()
    chat_placeholder = st.empty()

with col2:
    # Robot's view section
    st.subheader("Simulation Overview")
    sim_image = Image.open('sim.png')
    st.image(sim_image, caption="Robot's Point of View", use_column_width=True)

# Initialize session state
if 'paused' not in st.session_state:
    st.session_state.paused = False
if 'message_displayed' not in st.session_state:
    st.session_state.message_displayed = False
if 'robot_positions_current' not in st.session_state:
    st.session_state.robot_positions_current = {name: data["path"][0] for name, data in robots.items()}

# Button to control movement
if st.button('Acknowledge'):
    st.session_state.paused = False
    st.session_state.message_displayed = False

# JavaScript for blinking text
st.markdown("""
    <style>
    @keyframes blinker {
        50% { opacity: 0; }
    }
    .blinking {
        animation: blinker 1s linear infinite;
    }
    </style>
    """, unsafe_allow_html=True)

# Simulate robots' movement
while any(pos != path[-1] for name, (path, pos) in zip(robots.keys(), zip([data["path"] for data in robots.values()], st.session_state.robot_positions_current.values()))):
    if not st.session_state.paused:
        for robot_name, robot_data in robots.items():
            path = robot_data["path"]
            color = robot_data["color"]
            messages = robot_data["messages"]
            
            current_pos_index = path.index(st.session_state.robot_positions_current[robot_name])
            if current_pos_index < len(path) - 1:
                st.session_state.robot_positions_current[robot_name] = path[current_pos_index + 1]
                
                # Update the visible part of the path
                start_index = max(0, current_pos_index - 2)
                end_index = min(len(path), current_pos_index + 3)
                visible_path = path[start_index:end_index]
                path_x, path_y = zip(*visible_path)

                # Set opacities for fading effect
                opacities = [0.2, 0.5, 1.0, 0.5, 0.2][:len(path_x)]

                # Update the robot's path and position
                for trace in fig.data:
                    if trace.name == f'{robot_name} Path':
                        trace.x = path_x
                        trace.y = path_y
                        trace.marker = dict(size=6, opacity=opacities)
                    elif trace.name == robot_name:
                        trace.x = [st.session_state.robot_positions_current[robot_name][0]]
                        trace.y = [st.session_state.robot_positions_current[robot_name][1]]
                
                # Display the updated map
                with map_placeholder:
                    st.plotly_chart(fig)
        
                # Display communication messages
                with chat_placeholder:
                    if not st.session_state.message_displayed:
                        if st.session_state.robot_positions_current[robot_name] in messages:
                            st.markdown(f"<div class='blinking'>**{robot_name}:**</div>", unsafe_allow_html=True)
                            st.markdown(messages[st.session_state.robot_positions_current[robot_name]], unsafe_allow_html=True)
                            st.session_state.paused = True
                            st.session_state.message_displayed = True
                        else:
                            st.empty()
                # Wait for a while to simulate real-time movement
                time.sleep(1)
    else:
        # Display paused message
        with map_placeholder:
            st.plotly_chart(fig)
        with chat_placeholder:
            st.markdown("<div class='blinking'><b>Movement Paused. Click 'Acknowledge' to Resume.</b></div>", unsafe_allow_html=True)
        time.sleep(1)


#BLINK CHATBOX TEST1

# BLINK Chatbox V1
# # BLINK Chatbox V1

# import streamlit as st
# import plotly.graph_objects as go
# import time
# import random
# from datetime import datetime

# def generate_intermediate_path(start, end):
#     path = [start]
#     x1, y1 = start
#     x2, y2 = end
#     while (x1, y1) != (x2, y2):
#         if x1 < x2:
#             x1 += 1
#         elif x1 > x2:
#             x1 -= 1
#         if y1 < y2:
#             y1 += 1
#         elif y1 > y2:
#             y1 -= 1
#         path.append((x1, y1))
#     return path

# def generate_messages(path, robot_name, color):
#     messages = {}
#     num_points = len(path)
#     intervals = max(1, num_points // 6)  # Messages at every sixth of the path
#     for i in range(1, num_points):
#         if i % intervals == 0:
#             messages[path[i]] = f"<b>Alert! <span style='color:{color};'>{robot_name}</span> is delayed and has reached {path[i]}.</b>"
#     if path[-1] not in messages:
#         messages[path[-1]] = f"<b><span style='color:{color};'>{robot_name}</span> has reached its destination at {path[-1]}.</b>"
#     return messages

# def generate_obstacles(num_obstacles, robot_paths):
#     obstacles = []
#     for _ in range(num_obstacles):
#         x = random.randint(0, 50)
#         y = random.randint(0, 50)
#         if any((x, y) in path for path in robot_paths):
#             continue  # Skip if obstacle is on a robot's path
#         obstacles.append((x, y))
#     return obstacles

# # Define robots' start and end positions
# robot_positions = {
#     "Explorer Robot": {"start": (1, 1), "end": (25, 10)},
#     "Scout Robot": {"start": (14, 15), "end": (48, 35)},
#     "Surveyor Robot": {"start": (30, 26), "end": (47, 48)},
#     "Drone Robot": {"start": (4, 7), "end": (24, 35)}
# }

# # Define colors for robots
# colors = {
#     "Explorer Robot": "blue",
#     "Scout Robot": "green",
#     "Surveyor Robot": "purple",
#     "Drone Robot": "red"
# }

# # Create robots dictionary with paths, colors, and messages
# robots = {}
# all_paths = []
# for robot_name, pos in robot_positions.items():
#     path = generate_intermediate_path(pos["start"], pos["end"])
#     all_paths.append(path)
#     robots[robot_name] = {
#         "path": path,
#         "color": colors[robot_name],
#         "messages": generate_messages(path, robot_name, colors[robot_name])
#     }

# # Generate obstacles
# num_obstacles = 50
# obstacles = generate_obstacles(num_obstacles, all_paths)

# # Create a Plotly figure for the map
# fig = go.Figure()

# # Add obstacles to the map in a single trace
# obstacle_x, obstacle_y = zip(*obstacles) if obstacles else ([], [])
# fig.add_trace(go.Scatter(
#     x=obstacle_x, 
#     y=obstacle_y, 
#     mode='markers', 
#     marker=dict(size=10, color='brown', symbol='cross'), 
#     name='Obstacle'
# ))

# # Add the robots' paths and positions with enhanced styling
# for robot_name, robot_data in robots.items():
#     path = robot_data["path"]
#     color = robot_data["color"]
#     messages = robot_data["messages"]
    
#     fig.add_trace(go.Scatter(x=[], y=[], mode='lines+markers', line=dict(color=color, dash='dot'), marker=dict(size=6), name=f'{robot_name} Path'))
    
#     robot_position = path[0]
#     fig.add_trace(go.Scatter(
#         x=[robot_position[0]], 
#         y=[robot_position[1]], 
#         mode='markers+text', 
#         marker=dict(size=15, color=color, symbol='circle', line=dict(width=2, color='black')), 
#         text=[robot_name], 
#         textposition='top center', 
#         name=robot_name
#     ))

# fig.update_layout(
#     title='Enhanced Robots Navigation Map with Obstacles',
#     xaxis=dict(range=[0, 50], autorange=False, title='X Coordinate'),
#     yaxis=dict(range=[0, 50], autorange=False, title='Y Coordinate'),
#     width=1200,
#     height=900,
#     paper_bgcolor='lightgrey',  # Changed to light grey
#     plot_bgcolor='white',
#     showlegend=True
# )

# # Layout: Map above, Chat below
# map_placeholder = st.empty()
# chat_placeholder = st.empty()
# acknowledgment_placeholder = st.empty()

# # Simulate robots' movement
# robot_positions_current = {name: data["path"][0] for name, data in robots.items()}
# paused = False
# alerts_to_acknowledge = []
# current_alert = None

# def blink_message(message):
#     return f"""
#     <style>
#     @keyframes blinker {{
#         50% {{ opacity: 0; }}
#     }}
#     .blinking {{
#         animation: blinker 1s linear infinite;
#     }}
#     </style>
#     <div class="blinking">{message}</div>
#     """

# while any(pos != path[-1] for name, (path, pos) in zip(robots.keys(), zip([data["path"] for data in robots.values()], robot_positions_current.values()))):
#     for robot_name, robot_data in robots.items():
#         path = robot_data["path"]
#         color = robot_data["color"]
#         messages = robot_data["messages"]
        
#         current_pos_index = path.index(robot_positions_current[robot_name])
#         if current_pos_index < len(path) - 1:
#             robot_positions_current[robot_name] = path[current_pos_index + 1]
            
#             # Update the visible part of the path
#             start_index = max(0, current_pos_index - 2)
#             end_index = min(len(path), current_pos_index + 3)
#             visible_path = path[start_index:end_index]
#             path_x, path_y = zip(*visible_path)

#             # Set opacities for fading effect
#             opacities = [0.2, 0.5, 1.0, 0.5, 0.2][:len(path_x)]  # Adjust the opacity length to visible path length

#             # Update the robot's path and position
#             for trace in fig.data:
#                 if trace.name == f'{robot_name} Path':
#                     trace.x = path_x
#                     trace.y = path_y
#                     trace.marker = dict(size=6, opacity=opacities)
#                 elif trace.name == robot_name:
#                     trace.x = [robot_positions_current[robot_name][0]]
#                     trace.y = [robot_positions_current[robot_name][1]]
            
#             # Display the updated map
#             with map_placeholder:
#                 st.plotly_chart(fig)
    
#             # Check for new alerts
#             if robot_positions_current[robot_name] in messages:
#                 if current_alert != (robot_name, robot_positions_current[robot_name]):
#                     alerts_to_acknowledge.append(messages[robot_positions_current[robot_name]])
#                     current_alert = (robot_name, robot_positions_current[robot_name])
            
#             # Display acknowledgment button if there are alerts
#             if alerts_to_acknowledge:
#                 with acknowledgment_placeholder:
#                     st.markdown(blink_message("Click 'Acknowledge' to continue."), unsafe_allow_html=True)
#                     if st.button("Acknowledge"):
#                         alerts_to_acknowledge.pop(0)
#                         current_alert = None
#                         acknowledgment_placeholder.empty()
            
#             # Display current alert if there is one
#             if alerts_to_acknowledge:
#                 with chat_placeholder:
#                     st.markdown(f"**{robot_name}:**")
#                     st.markdown(blink_message(alerts_to_acknowledge[0]), unsafe_allow_html=True)
#             else:
#                 st.empty()
    
#             # Wait for a while to simulate real-time movement
#             time.sleep(0.3)







# import streamlit as st
# import plotly.graph_objects as go
# import time

# # Define robots' paths and messages
# robots = {
#     "Explorer Robot": {
#         "path": [(1, 1), (8, 8), (15, 14), (20, 22), (22, 25), (25, 30)],
#         "color": "blue",
#         "messages": {(8, 8): "Alert! Explorer Robot has reached (8, 8) later than expected!",
#                      (15, 14): "Alert! Explorer Robot has reached (15, 14) later than expected!",
#                      (20, 22): "Alert! Explorer Robot has reached (20, 22) later than expected!"}
#     },
#     "Scout Robot": {
#         "path": [(32, 25), (34, 27), (36, 30), (38, 32), (40, 35), (38, 37), (36, 39), (35, 39), (40, 40)],
#         "color": "green",
#         "messages": {(34, 27): "Alert! Scout Robot has reached (34, 27) later than expected!",
#                      (38, 32): "Alert! Scout Robot has reached (38, 32) later than expected!",
#                      (36, 39): "Alert! Scout Robot has reached (36, 39) later than expected!"}
#     },
#     "Surveyor Robot": {
#         "path": [(17, 29), (19, 25), (21, 23), (23, 24), (26, 26), (28, 27), (30, 30)],
#         "color": "purple",
#         "messages": {(19, 25): "Alert! Surveyor Robot has reached (19, 25) later than expected!",
#                      (23, 24): "Alert! Surveyor Robot has reached (23, 24) later than expected!",
#                      (28, 27): "Alert! Surveyor Robot has reached (28, 27) later than expected!"}
#     },
#     "Drone Robot": {
#         "path": [(12, 12), (15, 15), (18, 18), (20, 20), (22, 22), (24, 24), (26, 26), (28, 28), (30, 30), (32, 32), (34, 34), (24, 24)],
#         "color": "red",
#         "messages": {(15, 15): "Alert! Drone Robot has reached (15, 15) later than expected!",
#                      (20, 20): "Alert! Drone Robot has reached (20, 20) later than expected!",
#                      (24, 24): "Alert! Drone Robot has reached (24, 24) later than expected!"}
#     }
# }

# # Create a Plotly figure for the map
# fig = go.Figure()

# # Define grid size
# grid_size = 50

# # Add the grid lines
# for i in range(0, grid_size + 1, 1):
#     fig.add_trace(go.Scatter(x=[i, i], y=[0, grid_size], mode='lines', line=dict(color='lightgrey', width=0.5), showlegend=False))
#     fig.add_trace(go.Scatter(x=[0, grid_size], y=[i, i], mode='lines', line=dict(color='lightgrey', width=0.5), showlegend=False))

# # Add the robots' paths and positions
# for robot_name, robot_data in robots.items():
#     path = robot_data["path"]
#     color = robot_data["color"]
#     messages = robot_data["messages"]
    
#     path_x, path_y = zip(*path)
#     fig.add_trace(go.Scatter(x=path_x, y=path_y, mode='lines+markers', line=dict(color=color, dash='dash'), marker=dict(size=5), name=f'{robot_name} Path'))
    
#     # Initialize the robot's starting position
#     robot_position = path[0]
#     fig.add_trace(go.Scatter(
#         x=[robot_position[0]],
#         y=[robot_position[1]],
#         mode='markers',
#         marker=dict(symbol='diamond', size=10, color=color),
#         name=f'{robot_name} Start'
#     ))
    
#     # Add end point
#     end_position = path[-1]
#     fig.add_trace(go.Scatter(
#         x=[end_position[0]],
#         y=[end_position[1]],
#         mode='markers',
#         marker=dict(symbol='x', size=12, color=color, line=dict(color='black', width=2)),
#         name=f'{robot_name} End'
#     ))

# # Set figure layout
# fig.update_layout(
#     title='Custom World Map with Robots',
#     xaxis=dict(range=[0, grid_size], autorange=False),
#     yaxis=dict(range=[0, grid_size], autorange=False),
#     width=800,
#     height=800,
#     showlegend=True
# )

# # Streamlit interface
# st.title("Custom World Map with Robots")
# map_placeholder = st.empty()
# chat_placeholder = st.empty()

# # Simulate robots' movement
# robot_positions = {name: data["path"][0] for name, data in robots.items()}
# while any(pos != path[-1] for name, (path, pos) in zip(robots.keys(), zip([data["path"] for data in robots.values()], robot_positions.values()))):
#     for robot_name, robot_data in robots.items():
#         path = robot_data["path"]
#         color = robot_data["color"]
#         messages = robot_data["messages"]
        
#         current_pos_index = path.index(robot_positions[robot_name])
#         if current_pos_index < len(path) - 1:
#             robot_positions[robot_name] = path[current_pos_index + 1]
#             # Update the robot's position
#             for trace in fig.data:
#                 if trace.name == f'{robot_name} Start':
#                     trace.x = [robot_positions[robot_name][0]]
#                     trace.y = [robot_positions[robot_name][1]]
            
#             # Display the updated map
#             with map_placeholder:
#                 st.plotly_chart(fig)
    
#             # Display communication messages
#             with chat_placeholder:
#                 st.write(f"{robot_name}:")
#                 if robot_positions[robot_name] in messages:
#                     st.text(messages[robot_positions[robot_name]])
#                 else:
#                     st.empty()

#             # Wait for a while to simulate real-time movement
#             time.sleep(1)





# import streamlit as st
# import plotly.graph_objects as go
# import time
# import random

# # Define robots' paths and messages
# robots = {
#     "Explorer Robot": {
#         "path": [(1, 1), (8, 8), (15, 14), (20, 22), (22, 25), (25, 30)],
#         "color": "blue",
#         "messages": {(8, 8): "Alert! Explorer Robot has reached (8, 8) later than expected!",
#                      (15, 14): "Alert! Explorer Robot has reached (15, 14) later than expected!",
#                      (20, 22): "Alert! Explorer Robot has reached (20, 22) later than expected!"}
#     },
#     "Scout Robot": {
#         "path": [(32, 25), (34, 27), (36, 30), (38, 32), (40, 35), (38, 37), (36, 39), (35, 39), (40, 40)],
#         "color": "green",
#         "messages": {(34, 27): "Alert! Scout Robot has reached (34, 27) later than expected!",
#                      (38, 32): "Alert! Scout Robot has reached (38, 32) later than expected!",
#                      (36, 39): "Alert! Scout Robot has reached (36, 39) later than expected!"}
#     },
#     "Surveyor Robot": {
#         "path": [(17, 29), (19, 25), (21, 23), (23, 24), (26, 26), (28, 27), (30, 30)],
#         "color": "purple",
#         "messages": {(19, 25): "Alert! Surveyor Robot has reached (19, 25) later than expected!",
#                      (23, 24): "Alert! Surveyor Robot has reached (23, 24) later than expected!",
#                      (28, 27): "Alert! Surveyor Robot has reached (28, 27) later than expected!"}
#     },
#     "Drone Robot": {
#         "path": [(12, 12), (15, 15), (18, 18), (20, 20), (22, 22), (24, 24), (26, 26), (28, 28), (30, 30), (32, 32), (34, 34), (24, 24)],
#         "color": "red",
#         "messages": {(15, 15): "Alert! Drone Robot has reached (15, 15) later than expected!",
#                      (20, 20): "Alert! Drone Robot has reached (20, 20) later than expected!",
#                      (24, 24): "Alert! Drone Robot has reached (24, 24) later than expected!"}
#     }
# }

# # Find all path points
# all_path_points = set()
# for robot_data in robots.values():
#     all_path_points.update(robot_data["path"])

# # Function to generate a unique end point
# def generate_unique_end_point(existing_points):
#     while True:
#         x = random.randint(0, 50)
#         y = random.randint(0, 50)
#         if (x, y) not in existing_points:
#             return (x, y)

# # Update end points
# for robot_data in robots.values():
#     end_position = generate_unique_end_point(all_path_points)
#     robot_data["path"][-1] = end_position
#     all_path_points.add(end_position)

# # Create a Plotly figure for the map
# fig = go.Figure()

# # Define grid size and map size
# grid_size = 50
# map_size = 600  # Map size in pixels

# # Add the grid lines
# for i in range(0, grid_size + 1, 1):
#     fig.add_trace(go.Scatter(x=[i, i], y=[0, grid_size], mode='lines', line=dict(color='lightgrey', width=0.5), showlegend=False))
#     fig.add_trace(go.Scatter(x=[0, grid_size], y=[i, i], mode='lines', line=dict(color='lightgrey', width=0.5), showlegend=False))

# # Add the robots' paths and positions
# for robot_name, robot_data in robots.items():
#     path = robot_data["path"]
#     color = robot_data["color"]
#     messages = robot_data["messages"]
    
#     path_x, path_y = zip(*path)
#     fig.add_trace(go.Scatter(x=path_x, y=path_y, mode='lines+markers', line=dict(color=color, dash='dash'), marker=dict(size=5), name=f'{robot_name} Path'))
    
#     # Initialize the robot's starting position
#     robot_position = path[0]
#     fig.add_trace(go.Scatter(
#         x=[robot_position[0]],
#         y=[robot_position[1]],
#         mode='markers',
#         marker=dict(symbol='diamond', size=10, color=color),
#         name=f'{robot_name} Start'
#     ))
    
#     # Add end point
#     end_position = path[-1]
#     fig.add_trace(go.Scatter(
#         x=[end_position[0]],
#         y=[end_position[1]],
#         mode='markers',
#         marker=dict(symbol='x', size=12, color=color, line=dict(color='black', width=2)),
#         name=f'{robot_name} End'
#     ))

# # Set figure layout
# fig.update_layout(
#     title='Custom World Map with Robots',
#     xaxis=dict(range=[0, grid_size], autorange=False),
#     yaxis=dict(range=[0, grid_size], autorange=False),
#     width=map_size,
#     height=map_size,
#     showlegend=True
# )

# # Streamlit interface
# st.title("Custom World Map with Robots")

# # Layout adjustment
# col1, col2 = st.columns([2, 1])

# with col1:
#     map_placeholder = st.empty()
    
# with col2:
#     chat_placeholder = st.empty()

# # Simulate robots' movement
# robot_positions = {name: data["path"][0] for name, data in robots.items()}
# while any(pos != path[-1] for name, (path, pos) in zip(robots.keys(), zip([data["path"] for data in robots.values()], robot_positions.values()))):
#     for robot_name, robot_data in robots.items():
#         path = robot_data["path"]
#         color = robot_data["color"]
#         messages = robot_data["messages"]
        
#         current_pos_index = path.index(robot_positions[robot_name])
#         if current_pos_index < len(path) - 1:
#             robot_positions[robot_name] = path[current_pos_index + 1]
#             # Update the robot's position
#             for trace in fig.data:
#                 if trace.name == f'{robot_name} Start':
#                     trace.x = [robot_positions[robot_name][0]]
#                     trace.y = [robot_positions[robot_name][1]]
            
#             # Display the updated map
#             with map_placeholder:
#                 st.plotly_chart(fig, use_container_width=True)
    
#             # Display communication messages
#             with chat_placeholder:
#                 st.write(f"{robot_name}:")
#                 if robot_positions[robot_name] in messages:
#                     st.text(messages[robot_positions[robot_name]])
#                 else:
#                     st.empty()

#             # Wait for a while to simulate real-time movement
#             time.sleep(1)


# import streamlit as st
# import plotly.graph_objects as go
# import time
# import numpy as np

# # Define robots' paths and messages
# robots = {
#     "Explorer Robot": {
#         "path": [(1, 1), (2, 3), (3, 5), (4, 7), (5, 9), (6, 11), (7, 13), (8, 15), (9, 17), (10, 19), (11, 21), (12, 23), (13, 25), (14, 27), (15, 29), (16, 30), (17, 31), (18, 32), (19, 33), (20, 34)],
#         "color": "blue",
#         "messages": {(10, 19): "Alert! Explorer Robot has reached (10, 19) later than expected!",
#                      (15, 29): "Alert! Explorer Robot has reached (15, 29) later than expected!",
#                      (20, 34): "Alert! Explorer Robot has reached (20, 34) later than expected!"}
#     },
#     "Scout Robot": {
#         "path": [(2, 5), (3, 7), (4, 9), (5, 11), (6, 13), (7, 15), (8, 17), (9, 19), (10, 21), (11, 23), (12, 25), (13, 27), (14, 29), (15, 31), (16, 33), (17, 35), (18, 37), (19, 39), (20, 40)],
#         "color": "green",
#         "messages": {(10, 21): "Alert! Scout Robot has reached (10, 21) later than expected!",
#                      (15, 31): "Alert! Scout Robot has reached (15, 31) later than expected!",
#                      (20, 40): "Alert! Scout Robot has reached (20, 40) later than expected!"}
#     },
#     "Surveyor Robot": {
#         "path": [(3, 6), (4, 8), (5, 10), (6, 12), (7, 14), (8, 16), (9, 18), (10, 20), (11, 22), (12, 24), (13, 26), (14, 28), (15, 30), (16, 32), (17, 34), (18, 36), (19, 38), (20, 40)],
#         "color": "purple",
#         "messages": {(10, 20): "Alert! Surveyor Robot has reached (10, 20) later than expected!",
#                      (15, 30): "Alert! Surveyor Robot has reached (15, 30) later than expected!",
#                      (20, 40): "Alert! Surveyor Robot has reached (20, 40) later than expected!"}
#     },
#     "Drone Robot": {
#         "path": [(4, 7), (5, 9), (6, 11), (7, 13), (8, 15), (9, 17), (10, 19), (11, 21), (12, 23), (13, 25), (14, 27), (15, 29), (16, 31), (17, 33), (18, 35), (19, 37), (20, 39)],
#         "color": "red",
#         "messages": {(10, 19): "Alert! Drone Robot has reached (10, 19) later than expected!",
#                      (15, 29): "Alert! Drone Robot has reached (15, 29) later than expected!",
#                      (20, 39): "Alert! Drone Robot has reached (20, 39) later than expected!"}
#     }
# }

# # Helper function to find the closest point in the path
# def find_closest_point(current_pos, path):
#     path_np = np.array(path)
#     distances = np.sqrt(np.sum((path_np - np.array(current_pos))**2, axis=1))
#     return path[np.argmin(distances)]

# # Create a Plotly figure for the map
# fig = go.Figure()

# # Add the grid lines
# for i in range(0, 41, 1):  # 40x40 grid for a square map
#     fig.add_trace(go.Scatter(x=[i, i], y=[0, 40], mode='lines', line=dict(color='lightgrey', width=0.5), showlegend=False))
#     fig.add_trace(go.Scatter(x=[0, 40], y=[i, i], mode='lines', line=dict(color='lightgrey', width=0.5), showlegend=False))

# # Add the robots' paths and positions
# for robot_name, robot_data in robots.items():
#     path = robot_data["path"]
#     color = robot_data["color"]
#     messages = robot_data["messages"]
    
#     path_x, path_y = zip(*path)
#     fig.add_trace(go.Scatter(x=path_x, y=path_y, mode='lines+markers', line=dict(color=color, dash='dash'), marker=dict(size=5), name=f'{robot_name} Path'))
    
#     # Initialize the robot's starting position
#     robot_position = path[0]
#     robot_trace = go.Scatter(x=[robot_position[0]], y=[robot_position[1]], mode='markers', marker=dict(symbol='diamond', size=10, color=color), name=robot_name)
#     fig.add_trace(robot_trace)

# # Set figure layout with reduced size for the map
# fig.update_layout(
#     title='Custom World Map with Robots',
#     xaxis=dict(range=[0, 40], autorange=False),
#     yaxis=dict(range=[0, 40], autorange=False),
#     width=800,  # Adjusted width
#     height=600, # Adjusted height
#     showlegend=True
# )

# # Streamlit interface
# st.title("Custom World Map with Robots")

# # Layout: Map above, Chat below
# map_placeholder = st.empty()
# chat_placeholder = st.empty()

# # Simulate robots' movement
# robot_positions = {name: data["path"][0] for name, data in robots.items()}
# while any(pos != path[-1] for name, (path, pos) in zip(robots.keys(), zip([data["path"] for data in robots.values()], robot_positions.values()))):
#     for robot_name, robot_data in robots.items():
#         path = robot_data["path"]
#         color = robot_data["color"]
#         messages = robot_data["messages"]
        
#         current_pos = robot_positions[robot_name]
#         next_pos = find_closest_point(current_pos, path)
        
#         if next_pos != current_pos:
#             # Move robot towards the next position
#             if current_pos[0] < next_pos[0]:
#                 robot_positions[robot_name] = (current_pos[0] + 1, current_pos[1])
#             elif current_pos[0] > next_pos[0]:
#                 robot_positions[robot_name] = (current_pos[0] - 1, current_pos[1])
#             elif current_pos[1] < next_pos[1]:
#                 robot_positions[robot_name] = (current_pos[0], current_pos[1] + 1)
#             elif current_pos[1] > next_pos[1]:
#                 robot_positions[robot_name] = (current_pos[0], current_pos[1] - 1)

#             # Update the robot's position
#             for trace in fig.data:
#                 if trace.name == robot_name:
#                     trace.x = [robot_positions[robot_name][0]]
#                     trace.y = [robot_positions[robot_name][1]]
            
#             # Display the updated map
#             with map_placeholder:
#                 st.plotly_chart(fig)
    
#             # Display communication messages
#             with chat_placeholder:
#                 st.write(f"{robot_name}:")
#                 if robot_positions[robot_name] in messages:
#                     st.text(messages[robot_positions[robot_name]])
#                 else:
#                     st.empty()

#             # Wait for a while to simulate real-time movement
#             time.sleep(0.5)  # Adjust the speed as needed




# import streamlit as st
# import plotly.graph_objects as go
# import time
# import random

# # Define the robots' paths
# robots = {
#     'Commander Robot': {'path': [(0, 0), (5, 5), (10, 10), (11, 12), (13, 17), (15, 18), (18, 19), (20, 20)], 'color': 'red'},
#     'Explorer Robot': {'path': [(0, 50), (10, 40), (20, 30), (25, 35), (30, 40), (40, 30), (45, 20), (50, 10)], 'color': 'blue'},
#     'Scout Robot': {'path': [(50, 0), (45, 5), (40, 10), (35, 15), (30, 20), (25, 25), (20, 30), (10, 40)], 'color': 'green'},
#     'Surveyor Robot': {'path': [(50, 50), (45, 45), (40, 40), (35, 35), (30, 30), (25, 25), (20, 20), (10, 10)], 'color': 'purple'}
# }

# # Randomly allocate 3 points for each robot to send messages
# for robot in robots:
#     path = robots[robot]['path']
#     checkpoints = random.sample(path[1:-1], 3)  # Avoid the start and end points
#     robots[robot]['messages'] = {point: f"Alert! {robot} has reached {point} later than expected!" for point in checkpoints}

# # Create a Plotly figure for the map
# fig = go.Figure()

# # Add the grid lines
# for i in range(0, 51, 1):
#     fig.add_trace(go.Scatter(x=[i, i], y=[0, 50], mode='lines', line=dict(color='lightgrey', width=0.5), showlegend=False))
#     fig.add_trace(go.Scatter(x=[0, 50], y=[i, i], mode='lines', line=dict(color='lightgrey', width=0.5), showlegend=False))

# # Add the robots' paths and initialize their starting positions
# robot_traces = {}
# for robot, data in robots.items():
#     path_x, path_y = zip(*data['path'])
#     fig.add_trace(go.Scatter(x=path_x, y=path_y, mode='lines+markers', line=dict(color=data['color'], dash='dash'), marker=dict(size=5), name=f'{robot} Path'))
#     robot_traces[robot] = go.Scatter(x=[data['path'][0][0]], y=[data['path'][0][1]], mode='markers', marker=dict(symbol='diamond', size=10, color=data['color']), name=robot)
#     fig.add_trace(robot_traces[robot])

# # Set figure layout
# fig.update_layout(
#     title='Custom World Map with Robots',
#     xaxis=dict(range=[0, 50], autorange=False),
#     yaxis=dict(range=[0, 50], autorange=False),
#     width=600,
#     height=600,
#     showlegend=True
# )

# # Streamlit interface
# st.title("Custom World Map with Robots")
# map_placeholder = st.empty()
# chat_placeholder = st.empty()

# # Simulate robots' movement
# for i in range(len(list(robots.values())[0]['path'])):
#     chat_messages = []
#     for robot, data in robots.items():
#         path = data['path']
#         if i < len(path):
#             robot_position = path[i]
#             fig.data[-(4 - list(robots.keys()).index(robot))].x = [robot_position[0]]
#             fig.data[-(4 - list(robots.keys()).index(robot))].y = [robot_position[1]]
#             if robot_position in data['messages']:
#                 chat_messages.append(data['messages'][robot_position])
    
#     # Display the updated map
#     with map_placeholder:
#         st.plotly_chart(fig)
    
#     # Display communication messages
#     with chat_placeholder:
#         if chat_messages:
#             st.text('\n'.join(chat_messages))
#         else:
#             st.empty()

#     # Wait for a while to simulate real-time movement
#     time.sleep(1)



# import streamlit as st
# import plotly.graph_objects as go
# import time
# import random

# # Define the robots' paths
# robots = {
#     'Commander Robot': {'path': [(0, 0), (5, 5), (10, 10), (11, 12), (13, 17), (15, 18), (18, 19), (20, 20)], 'color': 'red'},
#     'Explorer Robot': {'path': [(0, 50), (10, 40), (20, 30), (25, 35), (30, 40), (40, 30), (45, 20), (50, 10)], 'color': 'blue'},
#     'Scout Robot': {'path': [(50, 0), (45, 5), (40, 10), (35, 15), (30, 20), (25, 25), (20, 30), (10, 40)], 'color': 'green'},
#     'Surveyor Robot': {'path': [(50, 50), (45, 45), (40, 40), (35, 35), (30, 30), (25, 25), (20, 20), (10, 10)], 'color': 'purple'}
# }

# # Randomly allocate 3 points for each robot to send messages
# for robot in robots:
#     path = robots[robot]['path']
#     checkpoints = random.sample(path[1:-1], 3)  # Avoid the start and end points
#     robots[robot]['messages'] = {point: f"Alert! {robot} has reached {point} later than expected!" for point in checkpoints}

# # Create a Plotly figure for the map
# fig = go.Figure()

# # Add the grid lines
# for i in range(0, 51, 1):
#     fig.add_trace(go.Scatter(x=[i, i], y=[0, 50], mode='lines', line=dict(color='lightgrey', width=0.5), showlegend=False))
#     fig.add_trace(go.Scatter(x=[0, 50], y=[i, i], mode='lines', line=dict(color='lightgrey', width=0.5), showlegend=False))

# # Add the robots' paths and initialize their starting positions
# robot_traces = {}
# for robot, data in robots.items():
#     path_x, path_y = zip(*data['path'])
#     fig.add_trace(go.Scatter(x=path_x, y=path_y, mode='lines+markers', line=dict(color=data['color'], dash='dash'), marker=dict(size=5), name=f'{robot} Path'))
#     robot_traces[robot] = go.Scatter(x=[data['path'][0][0]], y=[data['path'][0][1]], mode='markers', marker=dict(symbol='diamond', size=10, color=data['color']), name=robot)
#     fig.add_trace(robot_traces[robot])

# # Set figure layout
# fig.update_layout(
#     title='Custom World Map with Robots',
#     xaxis=dict(range=[0, 50], autorange=False),
#     yaxis=dict(range=[0, 50], autorange=False),
#     width=700,
#     height=500,
#     showlegend=True
# )

# # Streamlit interface
# st.title("Custom World Map with Robots")

# # Create a two-column layout
# col1, col2 = st.columns([3, 1])  # Adjust the ratios as needed

# # Map placeholder in the first column
# with col1:
#     map_placeholder = st.empty()

# # Chat box placeholder in the second column
# with col2:
#     chat_placeholder = st.empty()

# # Simulate robots' movement
# for i in range(len(list(robots.values())[0]['path'])):
#     chat_messages = []
#     for robot, data in robots.items():
#         path = data['path']
#         if i < len(path):
#             robot_position = path[i]
#             fig.data[-(4 - list(robots.keys()).index(robot))].x = [robot_position[0]]
#             fig.data[-(4 - list(robots.keys()).index(robot))].y = [robot_position[1]]
#             if robot_position in data['messages']:
#                 chat_messages.append(data['messages'][robot_position])
    
#     # Display the updated map
#     with map_placeholder:
#         st.plotly_chart(fig, use_container_width=True)
    
#     # Display communication messages
#     with chat_placeholder:
#         if chat_messages:
#             st.text('\n'.join(chat_messages))
#         else:
#             st.empty()

#     # Wait for a while to simulate real-time movement
#     time.sleep(1)


# import streamlit as st
# import plotly.graph_objects as go
# import time
# import random

# # Define the robots' paths
# robots = {
#     'Commander Robot': {'path': [(0, 0), (5, 5), (10, 10), (11, 12), (13, 17), (15, 18), (18, 19), (20, 20)], 'color': 'red'},
#     'Explorer Robot': {'path': [(0, 50), (10, 40), (20, 30), (25, 35), (30, 40), (40, 30), (45, 20), (50, 10)], 'color': 'blue'},
#     'Scout Robot': {'path': [(50, 0), (45, 5), (40, 10), (35, 15), (30, 20), (25, 25), (20, 30), (10, 40)], 'color': 'green'},
#     'Surveyor Robot': {'path': [(50, 50), (45, 45), (40, 40), (35, 35), (30, 30), (25, 25), (20, 20), (10, 10)], 'color': 'purple'}
# }

# # Randomly allocate 3 points for each robot to send messages
# for robot in robots:
#     path = robots[robot]['path']
#     checkpoints = random.sample(path[1:-1], 3)  # Avoid the start and end points
#     robots[robot]['messages'] = {point: f"Alert! {robot} has reached {point} later than expected!" for point in checkpoints}

# # Create a Plotly figure for the map
# fig = go.Figure()

# # Add the grid lines
# for i in range(0, 51, 1):
#     fig.add_trace(go.Scatter(x=[i, i], y=[0, 50], mode='lines', line=dict(color='lightgrey', width=0.5), showlegend=False))
#     fig.add_trace(go.Scatter(x=[0, 50], y=[i, i], mode='lines', line=dict(color='lightgrey', width=0.5), showlegend=False))

# # Add the robots' paths and initialize their starting positions
# for robot, data in robots.items():
#     path_x, path_y = zip(*data['path'])
#     fig.add_trace(go.Scatter(x=path_x, y=path_y, mode='lines+markers', line=dict(color=data['color'], dash='dash'), marker=dict(size=5), name=f'{robot} Path'))
# # Initialize robot icons
# robot_icons = {}
# for robot, data in robots.items():
#     robot_icons[robot] = go.Scatter(
#         x=[data['path'][0][0]],  # Corrected line: Removed extra quote
#         y=[data['path'][0][1]],  # Corrected line: Removed extra quote
#         mode='markers',
#         marker=dict(symbol='diamond', size=10, color=data['color']),
#         name=robot
#     )
#     fig.add_trace(robot_icons[robot])

# # Set figure layout
# fig.update_layout(
#     title='Custom World Map with Robots',
#     xaxis=dict(range=[0, 50], autorange=False),
#     yaxis=dict(range=[0, 50], autorange=False),
#     width=800,
#     height=600,
#     showlegend=True
# )

# # Streamlit interface
# st.title("Custom World Map with Robots")

# # Create a single-column layout
# st.subheader("Map")
# map_placeholder = st.empty()

# st.subheader("Chat")
# chat_placeholder = st.empty()

# # Simulate robots' movement
# for step in range(len(list(robots.values())[0]['path'])):
#     chat_messages = []
#     for robot, data in robots.items():
#         path = data['path']
#         if step < len(path):
#             robot_position = path[step]
#             # Update the robot's position in the icon trace
#             idx = list(robots.keys()).index(robot)
#             fig.data[len(robots) + idx].x = [robot_position[0]]
#             fig.data[len(robots) + idx].y = [robot_position[1]]
#             if robot_position in data['messages']:
#                 chat_messages.append(data['messages'][robot_position])
    
#     # Display the updated map
#     with map_placeholder:
#         st.plotly_chart(fig, use_container_width=True)
    
#     # Display communication messages
#     with chat_placeholder:
#         if chat_messages:
#             st.text('\n'.join(chat_messages))
#         else:
#             st.empty()

#     # Wait for a while to simulate real-time movement
#     time.sleep(1)


