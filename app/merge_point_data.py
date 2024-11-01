import geopandas as gpd

def merge_point_data(point_depths, events, points, catchment_dir):

    points_path = catchment_dir + 'Points/' + points + '.shp'

    critical_points = gpd.read_file(points_path)

    for i, event in enumerate(events):

        critical_points['D_' + event] = point_depths[i]
    
    critical_points.to_file(points_path)