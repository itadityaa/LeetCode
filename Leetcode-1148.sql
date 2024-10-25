SELECT DISTINCT t1.author_id as id
FROM Views t1
LEFT JOIN Views t2 ON t1.author_id = t2.author_id
WHERE t1.author_id = t2.viewer_id
ORDER BY t1.author_id